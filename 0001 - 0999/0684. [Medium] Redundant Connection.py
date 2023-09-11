# https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def helper(son):
            while parent[son] != son: 
                son = parent[son]
                
            return son 
        
        n = len(edges)
        
        parent = [i for i in range(n + 1)]
        
        for (u, v) in edges:             
            parentU = helper(u)
            parentV = helper(v)
            
            if parentU == parentV: 
                return (u, v)
            
            parent[parentU] = parent[parentV] = min(parentU, parentV)
            
class Solution2:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def helper(start, end):
            seen = {start: True}
            stack = [start]
            
            while stack: 
                u = stack.pop()
                for v in graph[u]:
                    if v not in seen: 
                        if v == end:                             
                            return True
                            
                        seen[v] = True
                        stack.append(v)
            
            return False
        
        graph = defaultdict(lambda: [])
        for (u, v) in edges:
            if helper(u, v):
                return [u, v]
                
            graph[u].append(v)
            graph[v].append(u)
            
        
