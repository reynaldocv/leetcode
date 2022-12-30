# https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        
        stack = [[0]]
        
        ans = []
        
        while stack: 
            way = stack.pop(0) 
            
            u = way[-1]
            
            if u == n - 1: 
                ans.append(way)
            else: 
                for v in graph[u]:
                    stack.append(way + [v])
                    
        return ans 
                
