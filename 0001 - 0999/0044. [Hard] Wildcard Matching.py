# https://leetcode.com/problems/wildcard-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def helper(i, j):
            if i == m and j == n: 
                return True 
            
            elif i == m or j == n: 
                if j != n and p[j] == "*":
                    if helper(i, j + 1):
                        return True 
                    
                return False 
            
            else: 
                if p[j] == "?":
                    if helper(i + 1, j + 1):
                        return True 
                    
                elif p[j] == "*":
                    if helper(i, j + 1) or helper(i + 1, j + 1) or helper(i + 1, j):
                        return True 
                    
                elif s[i] == p[j]:
                    return helper(i + 1, j + 1)
                
                else:                     
                    return False 
                
        m, n = len(s), len(p)
                
        return helper(0, 0)
                    
        
