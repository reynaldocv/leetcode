# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 
        
        if x < 0: 
            x *= -1 
            sign = -1 
            
        ans = sign * int(str(x)[::-1]) 
        
        if -(2**31) <= ans < 2**31:        
            return ans 
        
        else: 
            return 0 
