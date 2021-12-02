# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        start = 0 
        end = n - 1
        while start < end and s[start] == s[end]:
            while start + 1 < n and s[start + 1] == s[start]:
                start += 1
            while end - 1 >= 0 and s[end - 1] == s[end]:
                end -= 1
                
            start +=  1
            end -= 1
        
        return end - start + 1 if end - start + 1 > 0 else 0 
            
        
        
        
        
