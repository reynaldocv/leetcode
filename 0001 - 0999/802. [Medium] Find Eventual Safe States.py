# https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        @cache
        def helper(u):
            if color[u] != WHITE:
                return color[u] == BLACK
            
            color[u] = GRAY
            for v in graph[u]:
                if color[v] == BLACK: 
                    continue
                if color[v] == GRAY or not helper(v):
                    return False
                
            color[u] = BLACK
            
            return True        
        
        WHITE, GRAY, BLACK = 0, 1, 2
        
        color = defaultdict(lambda: 0)
        n = len(graph)
        
        ans = []
        
        for i in range(n):
            if helper(i):
                ans.append(i)
                
        return ans             
    
