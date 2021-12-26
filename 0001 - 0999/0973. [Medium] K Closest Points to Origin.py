# https://leetcode.com/problems/k-closest-points-to-origin/
    
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda item: item[0]**2 + item[1]**2)
        
        return points[:k]
        
        
            
        
        
        
