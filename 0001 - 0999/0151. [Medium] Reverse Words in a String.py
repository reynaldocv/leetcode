# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        
        word = ""
        
        for char in s + " ":
            if char == " ":
                if word != "":
                    arr.insert(0, word)
                    
                    word = ""
                    
            else: 
                word += char 
                
        return " ".join(arr)
