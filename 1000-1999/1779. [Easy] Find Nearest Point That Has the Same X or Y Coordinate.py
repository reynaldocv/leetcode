# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dic = {}
        min_ = (inf, -1)
        for i in range(len(points)): 
            a = points[i][0]
            b = points[i][1]
            if x == a or y == b:
                dist = abs(x - a) + abs(y - b)
                min_ = min(min_, (dist, i))
        
        return min_[1]
                
