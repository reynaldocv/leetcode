# https://leetcode.com/problems/consecutive-characters/

class Solution:
    def maxPower(self, s: str) -> int:
        prev = "$"         
        cnt = 1 
        
        ans = 0 
        
        for char in s: 
            if prev == char: 
                cnt += 1 
            else: 
                prev = char                
                cnt = 1 
            
            ans = max(ans, cnt)
                
        return ans 
