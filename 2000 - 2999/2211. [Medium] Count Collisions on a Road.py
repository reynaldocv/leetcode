# https://leetcode.com/problems/count-collisions-on-a-road/

class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        
        ans = 0 
        
        for direction in directions: 
            if direction != "S":
                ans += 1 
         
        left = 0 
        
        while left < n and directions[left] == "L":
            ans -= 1 
            
            left +=1 
            
        right = n - 1
        
        while right >= 0 and directions[right] == "R":
            ans -= 1 
            
            right -= 1 
            
        return ans 
    
                        
                        
        
        
