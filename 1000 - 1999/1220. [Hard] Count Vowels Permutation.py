# https://leetcode.com/problems/count-vowels-permutation/

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1 for _ in range(5)]
            
        for i in range(1, n):
            arr = []
            arr.append(dp[1] + dp[2] + dp[4])
            arr.append(dp[0] + dp[2])
            arr.append(dp[1] + dp[3])
            arr.append(dp[2])
            arr.append(dp[2] + dp[3])
            dp = arr
            
        return sum(dp) % MOD
        
        
       
