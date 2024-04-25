# https://leetcode.com/problems/longest-ideal-subsequence/

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        
        value = {chr(ord("a") + i): i for i in range(26)}
        
        dp = [[0 for _ in range(26)] for _  in range(n + 1)]
        
        for i in range(1, n + 1):
            val = value[s[i - 1]]
            
            for j in range(26):
                if val == j: 
                    for l in range(26):
                        if abs(val - l) <= k: 
                            dp[i][val] = max(dp[i][val], dp[i - 1][l] + 1)
                    
                else: 
                    dp[i][j] = dp[i - 1][j]
                    
        return max(dp[-1][i] for i in range(26))
        
        
                
        
