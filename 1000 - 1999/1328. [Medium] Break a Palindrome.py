# https://leetcode.com/problems/break-a-palindrome/

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1: 
            return ""
        
        idx = -1
        for i in range(n//2):
            if palindrome[i] != "a":
                idx = i
                break
      
        ans = ""
        if idx == -1:             
            ans = palindrome[:n - 1] + "b"
        else: 
            ans = palindrome[:idx] + "a" + palindrome[idx + 1:]
            
        return ans
            
        
