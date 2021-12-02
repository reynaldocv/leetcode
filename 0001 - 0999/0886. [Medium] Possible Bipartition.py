# https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def helper(u, turn):
            for v in graph[u]:
                if (v, turn) not in seen: 
                    seen[(v, turn)] = True
                    helper(v, not turn)
        
        graph = defaultdict(lambda: [])
        vertices = {}
        for (a, b) in dislikes: 
            graph[a].append(b)
            graph[b].append(a)
            vertices[a] = a
            vertices[b] = b
            
        seen = {}
        for u in vertices: 
            if (u, True) not in seen and (u, False) not in seen: 
                seen[(u, False)] = True
                helper(u, True)
                
        for (key, turn) in seen: 
            if (key, not turn) in seen: 
                return False
        
        return True
        
