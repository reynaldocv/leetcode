# https://leetcode.com/problems/base-7/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: 
            return "0"
        
        sign = "-" if num < 0 else ""
        num *= -1 if num < 0 else 1 
        
        ans = ""
        
        while num: 
            ans = str(num % 7) + ans
            
            num //= 7 
            
        return sign + ans 
            
