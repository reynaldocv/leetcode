# https://leetcode.com/problems/alternating-digit-sum/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0 
        
        time = 1
        
        while n:
            ans += (n % 10) if time else -(n % 10)
            
            time = 1 - time            
            n //= 10 
            
        return ans if time == 0 else -ans
