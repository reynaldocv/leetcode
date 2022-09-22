# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        seen = {chr(ord("a") + i) for i in range(26)}
    
        for i in range(10):
            seen.add(str(i))
        
        ans = ""
        
        for char in s: 
            letter = char.lower()
            if letter in seen: 
                ans += letter
                
        return ans == ans[:: -1]
            
