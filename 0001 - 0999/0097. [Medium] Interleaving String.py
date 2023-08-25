# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def helper(i, j, k):
            if i == m and j == n and k == l: 
                return True 
            
            else: 
                if i < m and k < l and s1[i] == s3[k]:
                    if helper(i + 1, j, k + 1):
                        return True 
                    
                if j < n and k < l and s2[j] == s3[k]:
                    if helper(i, j + 1, k + 1):
                        return True 
                    
                return False 
        
        m, n, l = len(s1), len(s2), len(s3)
        
        return helper(0, 0, 0)
    
class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        
        if m + n != l: 
            return False 
        
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        
        dp[0][0] = True 
        
        for i in range(m + 1):
            for j in range(n + 1):
                idx = i + j - 1
                
                if i >= 1 and s1[i - 1] == s3[idx] and dp[i - 1][j]:
                    dp[i][j] = True 
                
                if j >= 1 and s2[j - 1] == s3[idx] and dp[i][j - 1]:
                    dp[i][j] = True 
     
        return dp[-1][-1]
     
        
