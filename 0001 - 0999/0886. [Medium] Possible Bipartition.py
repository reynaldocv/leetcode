# https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def helper(u, color):
            if u in colors: 
                return colors[u] == color
            
            else: 
                colors[u] = color
                
                for v in graph[u]:
                    if helper(v, 1 - color) == False:
                        return False 
                    
                return True 
        
        graph = defaultdict(lambda: [])
        
        for (u, v) in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            
        colors = {}
            
        for i in range(1, n + 1):
            if i not in colors: 
                if helper(i, 1) == False:
                    return False 
                
        return True 
                    
        
