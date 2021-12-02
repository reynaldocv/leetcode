# https://leetcode.com/problems/goat-latin/

class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = "aeiouAEIOU"
        words = S.split(" ")
        n = len(words)
        for i in range(n):
            if words[i][0] in vowels: 
                words[i] += "ma"
            else:
                words[i] = words[i][1:] + words[i][0] + "ma"
            words[i] += "a"*(i + 1) 
        
        return " ".join(words)
