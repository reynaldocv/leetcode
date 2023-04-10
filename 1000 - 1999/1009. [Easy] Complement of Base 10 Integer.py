# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: 
            return 1 
        
        ans = 0 
        
        ratio = 1
        
        while n: 
            bit = n % 2
            
            ans += ratio*(1 - bit)
            
            n //= 2 
            ratio *= 2
            
        return ans 
                          
                    
        
