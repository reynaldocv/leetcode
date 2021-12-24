# https://leetcode.com/problems/circle-and-rectangle-overlapping/

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2: 
            return True
        
        for (x, y) in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]: 
            if (x - xCenter)**2 + (y - yCenter)**2 <= radius**2: 
                return True 
         
        for x in [x1, x2]: 
            if xCenter - radius <= x <= xCenter + radius and y1 <= yCenter <= y2: 
                return True
            
        for y in [y1, y2]:
            if yCenter - radius <= y <= yCenter + radius and x1 <= xCenter <= x2: 
                return True 
        
        return False  
