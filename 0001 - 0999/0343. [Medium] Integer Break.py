# https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0 for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
            
        for i in range(n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], (i - j)*j, (i - j)*dp[j])
        return dp[n]
        
        
        
        
        
