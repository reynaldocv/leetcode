# https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:        
        graph = [set([]) for _ in range(n)]
        for (v0, v1) in edges: 
            graph[v0].add(v1)
            graph[v1].add(v0)
            
        if start == end: 
            return True
        
        seen = {start: True}
        stack = [start]
        
        while stack:
            v0 = stack.pop(0)
            for v1 in graph[v0]:
                if v1 == end: 
                    return True
                if v1 not in seen: 
                    seen[v1] = True
                    stack.append(v1)
            
        return False
        
        
