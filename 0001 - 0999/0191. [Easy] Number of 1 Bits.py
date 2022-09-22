# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0 
        
        while n: 
            if (n % 2) == 1:
                ans += 1 
            
            n //= 2 
            
        return ans 
        
