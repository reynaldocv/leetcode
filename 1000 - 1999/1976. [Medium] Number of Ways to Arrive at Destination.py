# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        @cache
        def helper(u):
            if u == n - 1: 
                return 1 
            if distance[u] == inf: 
                return 0 
            
            ans = 0 
            for (v, time) in graph[u]:
                if distance[u] + time == distance[v]:
                    ans += helper(v)
                    
            return ans % MOD

        MOD = 10**9 + 7
        
        graph = defaultdict(lambda: [])
        for (u, v, time) in roads: 
            graph[u].append((v, time))
            graph[v].append((u, time))
            
        distance = [inf for _ in range(n)]
        distance[0] = 0 
        stack = [(0, 0)]
        
        while stack: 
            (u, t) = stack.pop()
            for (v, time) in graph[u]:
                if t + time < distance[v]:
                    distance[v] = t + time
                    stack.append((v, t + time))

        return helper(0)
