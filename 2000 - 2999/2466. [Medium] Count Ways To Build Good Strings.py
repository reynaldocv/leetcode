# https://leetcode.com/problems/count-ways-to-build-good-strings/

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        
        dp = [1] + [0 for _ in range(high)]
        
        for i in range(1, high + 1):
            for x in [zero, one]:
                start = i - x
                
                if start >= 0: 
                    dp[i] += dp[start]
                    
            dp[i] %= MOD
                    
        return sum(dp[low: high + 1]) % MOD
        
        
        
        
        
