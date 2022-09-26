# https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0     
        prev = ""
        
        for char in s + " ":
            if char == " ":
                if prev != "":
                    ans += 1 
                    
                prev = ""            
            else: 
                prev += char 
                
        return ans 
        
            
            
