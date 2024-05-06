# https://leetcode.com/problems/minimum-array-end/

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = 0
        
        idx = 0 
        
        n -= 1 
        
        while n or x:   
            if (x & 1) == 1: 
                ans ^=  (1 << idx)
                
            else: 
                bit = n % 2 
                
                if bit == 1:
                    ans ^= (1 << idx)
                
                n //= 2 
                
            x //= 2
            idx += 1 

        return ans 
                
        
