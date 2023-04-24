# https://leetcode.com/problems/sum-multiples/

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        
        for divisor in [3, 5, 7]:
            for i in range(divisor, n + 1, divisor):
                dp[i] = i 
                
        return sum(dp)
        
        
