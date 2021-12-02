# https://leetcode.com/problems/robot-bounded-in-circle/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        x, y, z = 0, 0, 0 
    
        for char in instructions: 
            if char == "G":
                x, y = x + directions[z][0], y + directions[z][1]
            elif char == "L":
                z = (z + 1) % 4
            else: 
                z = (z - 1) % 4
                
        return True if (x == 0 and y == 0) or z != 0 else False
            
        
