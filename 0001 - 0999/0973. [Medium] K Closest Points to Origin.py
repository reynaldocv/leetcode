# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return x**2 + y**2
        
        points.sort(key = lambda item: distance(item[0], item[1]))
        
        return points[:k]
            
        
        
        
