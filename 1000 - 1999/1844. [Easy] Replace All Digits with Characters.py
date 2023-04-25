# https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        
        n = len(s)
        
        for i in range(n//2):
            char = s[2*i]
            
            diff = int(s[2*i + 1])
            
            ans += char + chr(ord(char) + diff)
            
        if n % 2 == 1: 
            ans += s[-1]
            
        return ans 
    
        
