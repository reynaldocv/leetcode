# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = {letter for letter in brokenLetters}
        
        ans = 0 
        
        isTypeable = True 
        
        for char in text + " ":
            if char == " ":
                if isTypeable: 
                    ans += 1 
                
                isTypeable = True
                
            elif char in brokenLetters: 
                isTypeable = False
                
        return ans 
            
        
        
        
        
