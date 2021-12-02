#  https://leetcode.com/problems/valid-boomerang/ 

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x0, y0) = points[0]
        (x1, y1) = points[1]
        (x2, y2) = points[2]
        
        if (x0 - x1) != 0 and (x0 - x2):
            return (y0 - y2)/(x0 - x2) != (y0 - y1)/(x0 - x1)
        if (x1 - x2) != 0 and (x1 - x0):
            return (y1 - y2)/(x1 - x2) != (y1 - y0)/(x1 - x0)
        if (x2 - x0) != 0 and (x2 - x1):
            return (y2 - y0)/(x2 - x0) != (y2 - y1)/(x2 - x1)
        return False
        
        
        
