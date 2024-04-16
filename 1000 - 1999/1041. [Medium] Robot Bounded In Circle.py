# https://leetcode.com/problems/robot-bounded-in-circle/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        k = 0 
        
        (x, y) = (0, 0)
        
        for _ in range(4):
            for char in instructions: 
                if char == "G":
                    x, y = x + directions[k][0],  y + directions[k][1]
                    
                elif char == "L":
                    k = (k - 1) % 4
                    
                else: 
                    k = (k + 1) % 4
                    
        return x == 0 and y == 0
        
        
