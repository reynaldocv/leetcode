# https://leetcode.com/problems/maximal-network-rank/

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(lambda: [])
        
        for (a, b) in roads: 
            graph[a].append(b)
            graph[b].append(a)
        
        ans = 0 
        for u in range(1, n):
            for v in range(u):
                aux = len(graph[u]) + len(graph[v])
                if v in graph[u]:
                    aux -= 1 
                    
                ans = max(ans, aux)
                    
        return ans 
