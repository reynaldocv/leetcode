# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        
        for i in range(2, n +  1):             
            while i % 5 == 0:
                    i //= 5
                    
                    ans += 1 
                    
        return ans 
            
