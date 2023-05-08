# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        word1, word2 = s, s[:: -1]
        
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                
                else: 
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        return dp[-1][-1]
        
    
class Solution2:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache 
        def helper(start, end):
            if start > end: 
                return 0 
            
            elif start == end: 
                return 1 
            
            elif s[start] == s[end]:
                return 2 + helper(start + 1, end - 1)
            
            else: 
                return max(helper(start + 1, end), helper(start, end - 1))
            
        n = len(s)
        
        return helper(0, n - 1)
    
