# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        dp = [[0 for j in range(m)] for i in range(n)]
        
        dp[0][0] = ord(s1[0]) if s1[0] == s2[0] else 0
        
        for j in range(1, m):    
            dp[0][j] = ord(s1[0]) if s1[0] == s2[j] else dp[0][j - 1]
        
        for i in range(1, n):
            dp[i][0] = ord(s2[0]) if s1[i] == s2[0] else dp[i - 1][0]
            
        for i in range(1, n):
            for j in range(1, m):
                if s1[i] == s2[j]:
                    dp[i][j] = ord(s1[i]) + dp[i - 1][j - 1]
                else: 
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
            
        sum1 = sum([ord(s) for s in s1])
        sum2 = sum([ord(s) for s in s2])
        
        return sum1 + sum2 - 2*dp[n - 1][m - 1]
        
        
        
