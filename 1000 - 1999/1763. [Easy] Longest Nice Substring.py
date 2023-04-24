# https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        
        indexUpper = {chr(ord("A") + i): i for i in range(26)}
        indexLower = {chr(ord("a") + i): i for i in range(26)}
        
        ans = (0, 0, 1) 
        
        for i in range(n):
            lower = (0, )*26
            upper = (0, )*26
            
            for j in range(i, n):                    
                if s[j] in indexUpper:                     
                    idx = indexUpper[s[j]]
                    
                    upper = upper[: idx] + (1, ) + upper[idx + 1: ]
                    
                else: 
                    idx = indexLower[s[j]]
                    
                    lower = lower[: idx] + (1, ) + lower[idx + 1: ]
                    
                if lower == upper: 
                    ans = max(ans, (j - i + 1, -i, -j))
            
        return s[-ans[1]: -ans[2] + 1]
