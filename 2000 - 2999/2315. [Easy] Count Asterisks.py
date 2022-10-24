# https://leetcode.com/problems/count-asterisks/

class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt = 0 
        yes = True
        
        ans = 0 
        
        for char in s + "|":
            if char == "|":
                if yes:                 
                    ans += cnt 
                
                cnt = 0 
                yes = not yes
                
            elif char == "*":
                cnt += 1 
                
        return ans 
            
