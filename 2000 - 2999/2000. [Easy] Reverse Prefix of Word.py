# https://leetcode.com/problems/reverse-prefix-of-word/ 

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ""
        
        turn = 1 
        
        for (i, char) in enumerate(word): 
            if turn: 
                ans = char + ans
                
            else: 
                ans += char
            
            if char == ch and turn == 1:                                 
                turn = 1 - turn 
                
        if turn == 1:
            return word
        
        return ans 
        
        
