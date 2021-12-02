# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = [False for _ in range(n)]
        graph = [[] for _ in range(n)]
        for (u, v) in connections: 
            graph[u].append((v, 1))
            graph[v].append((u, 0))
            
        stack = [0]
        visited[0] = True
        ans = 0
        
        while stack: 
            u = stack.pop()
            for (v, changed) in graph[u]:
                if visited[v] == False: 
                    visited[v] = True
                    ans += changed
                    stack.append(v)
                    
        return ans
                
            
        
