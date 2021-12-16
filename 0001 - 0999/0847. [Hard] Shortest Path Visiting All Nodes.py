# https://leetcode.com/problems/shortest-path-visiting-all-nodes/

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        @cache
        def helper(u, mask):
            if mask == 0: 
                return 0 
            
            ans = inf
            for i in range(n):
                if mask & (1 << i) != 0: 
                    ans = min(ans, dist[u][i] + helper(i, mask ^ (1 << i)))
                    
            return ans
        
        n = len(graph)
        dist = [[inf for _ in range(n)] for _ in range(n)]
        
        for (i, u) in enumerate(graph):
            dist[i][i] = 0 
            for v in u: 
                dist[i][v] = 1
                
        for k in range(n): 
            for i in range(n): 
                for j in range(n): 
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        ans = inf
        for i in range(n):
            ans = min(ans, helper(i, (1 << n) - 1))
            
        return ans
