# https://leetcode.com/problems/decode-the-message/

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        letter = {" ": " "}
        
        i = 0 
        
        for char in key: 
            if char not in letter: 
                letter[char] = chr(ord("a") + i)
                
                i += 1 
        
        ans = ""
        
        for char in message: 
            ans += letter[char]
            
        return ans 
