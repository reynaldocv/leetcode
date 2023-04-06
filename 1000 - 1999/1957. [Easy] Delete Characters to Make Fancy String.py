# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        last = ["$", "0"]
        
        ans = ""
        
        for char in s: 
            if char == last[0]:
                if last[1] < 2: 
                    last[1] += 1 
                    ans += char
                
            else: 
                last = [char, 1]
                
                ans += char
                
        return ans 
            
                    
                    
