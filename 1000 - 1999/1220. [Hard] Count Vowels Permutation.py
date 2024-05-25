# https://leetcode.com/problems/count-vowels-permutation/

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1, 1, 1, 1, 1]
        
        for i in range(n - 1):
            newDp = [0, 0, 0, 0, 0]
            
            newDp[0] = (dp[1] + dp[2] + dp[4]) % MOD
            newDp[1] = (dp[0] + dp[2]) % MOD
            newDp[2] = (dp[1] + dp[3]) % MOD
            newDp[3] = (dp[2]) % MOD
            newDp[4] = (dp[2] + dp[3]) % MOD 
            
            dp = newDp
            
        return sum(dp) % MOD
            
        
