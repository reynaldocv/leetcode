# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def helper(u, even):
            for v in graph[u]:
                if (v, even) not in seen: 
                    seen[(v, even)] = True
                    helper(v, not even)
        
        seen = {}
        n = len(graph)
        
        for u in range(n):
            if (u, True) not in seen and (u, False) not in seen:
                seen[(u, False)] = True
                helper(u, True)
        
        for (u, v) in seen: 
            if (u, not v) in seen: 
                return False
        
        return True
        
