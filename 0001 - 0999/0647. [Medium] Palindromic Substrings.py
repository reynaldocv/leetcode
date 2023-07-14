# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        ans = 0 
        
        for i in range(n):
            start = i 
            end = i
            
            while 0 <= start and end < n and s[start] == s[end]:
                start -= 1 
                end += 1 
                
                ans += 1 
                
            start = i 
            end = i + 1
            
            while 0 <= start and end < n and s[start] == s[end]:
                start -= 1 
                end += 1 
                
                ans += 1 
            
        return ans 
            
        
