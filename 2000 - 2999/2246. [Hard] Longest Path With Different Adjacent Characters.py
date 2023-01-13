# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def helper(u):
            nonlocal ans 
            
            m0 = m1 = 0 
            
            for v in graph[u]:
                tmp = helper(v)
                
                if s[u] != s[v]:
                    if tmp >= m0: 
                        m0, m1 = tmp, m0
                    
                    elif tmp > m1: 
                        m1 = tmp 
                        
            ans = max(ans, 1 + m0 + m1)
            
            return 1 + m0
                
        graph = [[] for _ in parent]
        
        for (i, x) in enumerate(parent): 
            if x != -1: 
                graph[x].append(i)
        
        ans = 0
        
        helper(0)
        
        return ans
        
