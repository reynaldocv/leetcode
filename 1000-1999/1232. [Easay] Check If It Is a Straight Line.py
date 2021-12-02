# https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        k = []
        for i in range(1, len(coordinates)):
            count = 1
            dy = (coordinates[i][1]-coordinates[i-1][1])
            dx = (coordinates[i][0]-coordinates[i-1][0])
            if dx == 0:
                count = inf 
            else:
                count = dy/dx
                
            k.append(count)
            
        k = set(k)
        
        return True if len(k) == 1 else False
