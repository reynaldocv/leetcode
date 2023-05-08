# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        ans = (0, 0, 0)
        
        for i in range(n):
            start = i 
            end = i 
            
            while start >= 0 and end < n and s[start] == s[end]:
                start -= 1 
                end += 1 
                
            ans = max(ans, (end - start - 1, start + 1, end))
            
            start = i 
            end = i + 1
            
            while start >= 0 and end < n and s[start] == s[end]:
                start -= 1 
                end += 1 
            
            ans = max(ans, (end - start - 1, start + 1, end))
            
        return s[ans[1]: ans[2]]
            
            
                
