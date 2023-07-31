# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                    
                else: 
                    dp[i][j] = ord(s1[i - 1]) + ord(s2[j - 1]) + dp[i - 1][j - 1]
                    
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + ord(s1[i - 1]))                    
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + ord(s2[j - 1]))
                    
        return dp[-1][-1]
                    
class Solution2:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache 
        def helper(s1, s2):
            if s1 == "" or s2 == "":
                return sum(ord(char) for char in s1)  + sum(ord(char) for char in s2)
            
            else: 
                ans = ord(s1[0]) + helper(s1[1: ], s2)
                ans = min(ans, ord(s2[0]) + helper(s1, s2[1: ]))
                
                if s1[0] == s2[0]:
                    ans = min(ans, helper(s1[1: ], s2[1: ]))
                    
                return ans 
            
        return helper(s1, s2)
        
        
        
        
