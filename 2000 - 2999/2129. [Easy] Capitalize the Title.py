# https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        n = len(words)
        
        for i in range(n):
            if len(words[i]) <= 2: 
                words[i] = words[i].lower()
            else: 
                words[i] = words[i].capitalize()
                
        return " ".join(words)
        
