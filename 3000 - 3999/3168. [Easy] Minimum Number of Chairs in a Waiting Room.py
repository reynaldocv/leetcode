https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = 0 
        
        counter = 0 
        
        for char in s: 
            if char == "E":
                counter += 1 
                
            else: 
                counter -= 1 
                
            ans = max(ans, counter)
            
        return ans 
        
