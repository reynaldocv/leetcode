# https://leetcode.com/problems/reverse-prefix-of-word/ 

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = -1
        if ch in word: 
            idx = word.index(ch)
            
        if idx == -1:
            return word
        else: 
            return word[:idx + 1][::-1] + word[idx + 1:]
         
            
        
        
