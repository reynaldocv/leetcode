# https://leetcode.com/problems/wildcard-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def helper(i, j):
            if i == n and j == m: 
                return True
            elif j == m: 
                if s[i] == "*" and helper(i + 1, j):
                    return True
                
                return False
            elif i == n: 
                if p[j] == "*" and helper(i, j + 1):
                    return True
            
            elif s[i] == "*": 
                for jj in range(j, m + 1):
                    if helper(i + 1, jj):
                        return True
            elif p[j] == "*":
                for ii in range(i, n + 1):
                    if helper(ii, j + 1):
                        return True
            
            elif s[i] == "?" or p[j] == "?":
                if helper(i + 1, j + 1):
                    return True
            
            elif s[i] == p[j]:
                return helper(i + 1, j + 1)
            
            return False
        
        n, m = len(s), len(p)
        
        return helper(0, 0)
                
                
