# https://leetcode.com/problems/construct-the-rectangle/

class Solution:
    def constructRectangle(self, area: int) -> List[int]:     
        start = int(area**0.5)
        
        for width in range(start, 0, -1):
            if area % width == 0: 
                return [area//width, width]
        
        
        
