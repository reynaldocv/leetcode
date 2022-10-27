# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        counter = 0 
        
        ans = 0
        
        for char in s: 
            counter += 1 if char == "R" else -1 
            
            if counter == 0: 
                ans += 1 
                
        return ans 
                
        
        
