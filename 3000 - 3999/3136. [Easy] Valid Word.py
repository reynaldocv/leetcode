# https://leetcode.com/problems/valid-word/

class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        
        if n < 3: 
            return False 
        
        counter = [0, 0]
        
        chars = {chr(ord("a") + i) for i in range(26)}
        
        for char in word: 
            if char.isdigit(): 
                continue
                
            elif char.lower() in chars: 
                if char.lower() in "aeiou":
                    counter[0] = 1 
                    
                else: 
                    counter[1] = 1 
                    
            else: 
                return False 
            
        return sum(counter) >= 2
                
        
