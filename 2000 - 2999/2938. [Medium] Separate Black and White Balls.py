# https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0 
        
        tmp = 0 
        
        for (i, char) in enumerate(s[::-1]):
            if char == "1":
                ans += i - tmp 
                
                tmp += 1 
                
        return ans 
        
            
