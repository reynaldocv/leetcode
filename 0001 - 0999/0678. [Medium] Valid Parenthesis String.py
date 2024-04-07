# https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        left = 0 
        right = 0 
        
        for i in range(n):
            if s[i] == "(" or s[i] == "*":
                left += 1 
                
            else: 
                left -= 1                
        
            if s[n - 1 - i] == ")" or s[n - 1 - i] =="*":
                right += 1
                
            else: 
                right -= 1 
                
            if left < 0 or right < 0: 
                return False 
            
        return True 
