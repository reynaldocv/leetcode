# https://leetcode.com/problems/longest-happy-prefix/

class Solution:
    def longestPrefix(self, s: str) -> str:
        prefix = ""
        suffix = ""
        n = len(s)
        
        ans = ""
        
        for (i, char) in enumerate(s[:-1]): 
            prefix = prefix + char
            suffix = s[n - (i + 1)] + suffix
            
            if prefix == suffix: 
                ans = prefix
                
        return ans
          
