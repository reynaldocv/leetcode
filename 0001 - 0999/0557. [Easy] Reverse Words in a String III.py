# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        prev = ""
        
        for char in s + " ": 
            if char == " ":
                ans = ans + prev[::-1] + " "
                prev = ""
            else: 
                prev += char 
                
        return ans[: -1] 
        
            
        
