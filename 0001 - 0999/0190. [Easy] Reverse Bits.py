# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0 
        
        for i in range(32):
            bit = n % 2           
            ans = 2*ans + bit
            
            n //= 2
            
        return ans 
            
