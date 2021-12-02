# https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def route(start, end):
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
            if route(u, v):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)
            
        
