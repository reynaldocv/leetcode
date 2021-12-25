# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)    
        
        if n % 2 == 1: 
            return False
        
        noLocked = cnt = 0 
        
        for i in range(n):
            if locked[i] == "0":
                noLocked += 1
                
            elif s[i] == "(":
                cnt -= 1
                
            elif s[i] == ")":
                cnt += 1
            
            if noLocked < cnt: 
                return False
            
        noLocked = cnt = 0 
        
        for i in range(n - 1, -1, -1):
            if locked[i] == "0":
                noLocked += 1
                
            elif s[i] == "(":
                cnt += 1
                
            elif s[i] == ")":
                cnt -= 1
            
            if noLocked < cnt: 
                return False
        
        return True
            
        
        
        
