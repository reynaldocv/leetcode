# https://leetcode.com/problems/valid-square/

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(x0, y0, x1, y1):
            return ((x0 - x1)**2 + (y1 - y0)**2)**.5
        
        points = [p1, p2, p3, p4]
        distances = {}
        for i in range(4):
            for j in range(i + 1, 4):
                dist = distance(points[i][0], points[i][1], points[j][0], points[j][1])
                distances[dist] = distances.get(dist, 0) + 1
        
        if len(distances) == 2: 
            arr = [*distances]
            arr.sort()           
            return True if (distances[arr[0]] == 4 and distances[arr[1]] == 2) else False
        
        return False
                
