# https://leetcode.com/problems/construct-the-longest-new-string/

class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        xy = min(x, y)
        
        x -= xy
        y -= xy 
        
        ans = 4*xy + 2*z
        
        if x > 0 or y > 0:
            ans += 2 
            
        return ans 
        
