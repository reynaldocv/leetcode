# https://leetcode.com/problems/rearrange-spaces-between-words/

class Solution:
    def reorderSpaces(self, text: str) -> str:
        cnt = 0 
        
        words = []
        
        word = ""
        
        for char in text + " ":
            if char == " ":
                if word: 
                    words.append(word)
                
                word = ""
                
                cnt += 1 
                
            else: 
                word += char
                
        cnt -= 1 
                
        m = len(words)
        
        if m == 1: 
            return words[0] + " "*cnt
            
        else: 
            quotient = cnt//(m - 1)
            remain = cnt % (m - 1)
       
            return (" "*quotient).join(words) + " "*remain        
        
        
        
                
