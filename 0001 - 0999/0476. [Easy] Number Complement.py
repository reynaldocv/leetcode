# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0 
        base = 1 
        
        while num: 
            bit = num & 1 
            
            ans += (1 - bit)*base 
            
            base *= 2             
            num //= 2
            
        return ans 
        
            
