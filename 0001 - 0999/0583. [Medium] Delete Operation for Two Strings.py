# https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache 
        def helper(i, j):
            if i == m or j == n: 
                return 0 
            
            else: 
                ans = max(helper(i + 1, j), helper(i, j + 1))
                
                if word1[i] == word2[j]:
                    ans = max(ans, 1 + helper(i + 1, j + 1))
                    
                return ans 
                    
        m, n = len(word1), len(word2)
        
        return m + n - 2*helper(0, 0)
        
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1]  == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    
                else: 
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return m + n - 2*dp[-1][-1]
        
            
        
        
        
        
        
        
        
        
