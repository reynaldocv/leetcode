# https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() 
        
        s.sort() 
        
        m, n = len(g), len(s)
        
        i, j = 0, 0 
        
        ans = 0 
        
        while i < m and j < n: 
            if g[i] <= s[j]:
                ans += 1 
                i += 1 
                
            j += 1 
                
        return ans 
        
