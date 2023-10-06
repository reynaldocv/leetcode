# https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        def helper(n, m):
            base = n//m
            res = n % m 
            
            return (base + 1)**res*base**(m - res) 
            
        ans = 1
        
        for i in range(2, n):
            ans = max(ans, helper(n, i))
            
        return ans 
            
class Solution2:
    def integerBreak(self, n: int) -> int:
        dp = [0, 1] + [0 for _ in range(n - 1)]
            
        for i in range(n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], (i - j)*j, (i - j)*dp[j])
                
        return dp[n]
        
        
        
        
        
