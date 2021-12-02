# https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)        
        ans = [[0 for j in range(m)] for i in range(n)]
        
        ans[0][0] = 1 if word1[0] == word2[0] else 0 
        for j in range(1, m):
            ans[0][j] = 1 if word1[0] == word2[j] else ans[0][j - 1]
            
        for i in range(1, n):
            ans[i][0] = 1 if word1[i] == word2[0] else ans[i - 1][0]
            
        for i in range(1, n):
            for j in range(1, m):
                if word1[i] == word2[j]:
                    ans[i][j] = ans[i - 1][j - 1] + 1
                else: 
                    ans[i][j] = max(ans[i - 1][j], ans[i][j - 1], ans[i - 1][j - 1])
                    
        return n + m - 2*ans[n - 1][m - 1]
            
        
        
        
        
        
        
        
        
