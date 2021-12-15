# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(lambda: {})
        degree = defaultdict(lambda: 0)
        
        for (u, v) in edges: 
            graph[u][v] = graph[v][u] = True
            degree[u] += 1
            degree[v] += 1
        
        ans = inf
        for (u, v) in edges: 
            for w in range(max(u, v) + 1, n + 1):
                if w in graph[u] and w in graph[v]:
                    ans = min(ans, degree[u] + degree[v] + degree[w] - 6)
        
        return ans if ans == inf else -1   
        
        
        
