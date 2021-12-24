# https://leetcode.com/problems/distinct-subsequences-ii/

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        dp = [1]
        last = {}
        
        for (i, char) in enumerate(s):
            dp.append(dp[-1]*2)
            if char in last: 
                dp[-1] -= dp[last[char]]
            
            last[char] = i
            
        return (dp[-1] - 1) % MOD
            
