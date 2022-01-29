# https://leetcode.com/problems/last-substring-in-lexicographical-order/

class Solution:
    def lastSubstring(self, s: str) -> str:        
        ii = k = 0
        i = 1
        
        while i + k < len(s):
            if s[ii + k] == s[i + k]: 
                k += 1
            else: 
                if s[ii + k] > s[i + k]: 
                    i += k + 1
                else: 
                    ii = max(ii + k + 1, i)
                    i = ii + 1
                
                k = 0
                
        return s[ii:]
    
class Solution2:
    def lastSubstring(self, s: str) -> str:        
        ans = chr(ord("a") - 1)
        prefix = ""
        for char in s[::-1]:
            prefix = char + prefix
            ans = max(ans, prefix)
            
        return ans
            
