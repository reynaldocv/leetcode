# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = "$"
        ans = ""
        
        cnt = 1 
        
        for char in s: 
            if prev == char:
                cnt += 1 
                
            else: 
                cnt = 1 
                
            if cnt < 3:
                    ans += char 
                
            prev = char 
            
        return ans 
        
        
        
            
                    
                    
