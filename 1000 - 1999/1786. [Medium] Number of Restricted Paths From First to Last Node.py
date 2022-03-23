# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        @cache
        def helper(u): 
            if u == n-1: 
                return 1 
            
            ans = 0
            for (v, _) in graph[u]: 
                if distance[u] > distance[v]: 
                    ans += helper(v)
            
            return ans 
        
        MOD = 10**9 + 7
        
        graph = defaultdict(lambda: [])
        
        for (u, v, w) in edges: 
            graph[u - 1].append((v - 1, w))
            graph[v - 1].append((u - 1, w))
        
        heap = [(0, n-1)]
        distance = [inf for _ in range(n - 1)] + [0]
        
        while heap: 
            (dist, u) = heappop(heap)
            for (v, d) in graph[u]: 
                if distance[u] + d < distance[v]: 
                    distance[v] = distance[u] + d
                    heappush(heap, (distance[v], v))
        
        return helper(0) % MOD
