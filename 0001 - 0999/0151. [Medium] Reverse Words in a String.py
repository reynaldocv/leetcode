# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:        
        words = []
        word = ""
        n = len(s)
        for i in range(n):
            if s[i] != " ":
                word += s[i]
            elif word != "":
                words.append(word)
                word = ""
        
        if word != "":
            words.append(word)
            
        return " ".join(words[::-1])
                
        
