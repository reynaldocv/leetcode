# https://leetcode.com/problems/is-graph-bipartite/
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def helper(x, bit):
            stack = [(x, bit)]
            
            color[bit].add(x)
            
            while stack: 
                (x, bit) = stack.pop() 
                
                for y in graph[x]:
                    if y in color[bit]:
                        return False 
                    
                    if y not in color[1 - bit]:
                        stack.append((y, 1 - bit))
                        color[1 - bit].add(y)
                
            return True
            
        color = defaultdict(lambda: set())
        
        n = len(graph)
        
        for i in range(n):
            if i not in color[0] and i not in color[1]:
                if not helper(i, 0):
                    return False
                
        return True 
            
