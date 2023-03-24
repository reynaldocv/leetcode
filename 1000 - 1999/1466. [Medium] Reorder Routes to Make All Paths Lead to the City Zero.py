# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(lambda: {})
        
        for (a, b) in connections: 
            graph[a][b] = 1
            graph[b][a] = 0
            
        stack = [0]
        
        seen = {0}
        
        ans = 0 
        
        while stack: 
            u = stack.pop()
            
            for v in graph[u]:
                if v not in seen: 
                    seen.add(v)
                    stack.append(v)
                    
                    ans += graph[u][v]                    
                    
        return ans 
                
            
        
