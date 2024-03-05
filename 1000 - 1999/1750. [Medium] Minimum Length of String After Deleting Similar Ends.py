# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        
        start = 0 
        end = n - 1
                
        while start < end and s[start] == s[end]:
            char = s[start]
            
            while start <= end and s[start] == char: 
                start += 1 
            
            while start <= end and s[end] == char: 
                end -= 1 
          
        return end - start + 1
            
            
            
        
        
        
        
