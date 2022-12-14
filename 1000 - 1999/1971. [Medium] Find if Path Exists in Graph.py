# https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(lambda: [])
        
        for (u, v) in edges: 
            graph[u].append(v)
            graph[v].append(u)
            
        stack = [source]
        seen = {source}
        
        while stack:
            u = stack.pop()
            
            if u == destination: 
                return True
            
            for v in graph[u]:
                if v not in seen: 
                    seen.add(v)
                    stack.append(v)
                    
        return False
        
        
        
