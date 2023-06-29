# https://leetcode.com/problems/valid-square/

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        
        seen = set()
        
        for i in range(4):
            for j in range(i + 1, 4):
                distX = abs(points[i][0] - points[j][0])**2
                distY = abs(points[i][1] - points[j][1])**2
                
                seen.add(distX + distY)
                
        return 0 not in seen and len(seen) == 2
                
        
        
                
