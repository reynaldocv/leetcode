# https://leetcode.com/problems/path-crossing/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        (x, y) = (0, 0)
        
        seen = {(0, 0)}
        
        directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
        
        for char in path: 
            (r, s) = directions[char]
            
            x, y = x + r, y + s
            
            if (x, y) in seen: 
                return True 
            
            seen.add((x, y))
            
        return False 
        
