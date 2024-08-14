# https://leetcode.com/problems/snake-in-matrix/

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        (x, y) = (0, 0)
        
        for command in commands: 
            if command == "RIGHT":
                y += 1 
                
            elif command == "LEFT":
                y -= 1 
                
            elif command == "UP":
                x -= 1 
                
            else: 
                x += 1 
                
        return x*n + y
        
