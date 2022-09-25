# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        ans = 0 
        
        for char in s: 
            if char not in seen: 
                seen.add(char)
            else: 
                ans += 2 
                seen.remove(char)
                
        ans += 1 if seen else 0 
        
        return ans 
        
        
     
                
