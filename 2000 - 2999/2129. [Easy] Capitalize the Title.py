# https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        n = len(words)
        
        words = title.split(" ")
        
        for i in range(n):
            if len(words[i]) <= 2: 
                words[i] = words[i].lower()
                
            else: 
                words[i] = words[i].capitalize()
                
        return " ".join(words)
        
class Solution2:
    def capitalizeTitle(self, title: str) -> str:
        ans, tmp = "", ""
        
        for char in title + " ":
            if char == " ":
                if len(tmp) <= 2: 
                    ans += tmp.lower() + " "
                else: 
                    ans += tmp.capitalize() + " "
                tmp = ""
            
            else: 
                tmp += char
                
        return ans [: -1]
