# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: 
            return "0"
        
        if num < 0: 
            num += 2**32 
            
        letters = "0123456789abcdef"
        
        ans = ""
            
        while num > 0: 
            units = num % 16
            
            ans = letters[units] + ans
            
            num //= 16
            
        return ans
                
            
            
