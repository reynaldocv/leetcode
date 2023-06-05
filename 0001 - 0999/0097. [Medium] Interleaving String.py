# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache 
        def helper(s1, s2, s3):
            if s1 == s2 and s2 == s3 and s1 == "":
                return True 
            
            else: 
                ans = False 
                
                if s1 and s3 and s1[0] == s3[0]:
                    ans = ans or helper(s1[1: ], s2, s3[1: ])
                    
                if s2 and s3 and s2[0] == s3[0]:
                    ans = ans or helper(s1, s2[1: ], s3[1: ])
                    
                return ans 
            
        return helper(s1, s2, s3)
    
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
     
        
