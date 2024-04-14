# https://leetcode.com/problems/minimum-rectangles-to-cover-points/

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        
        last = -inf 
        
        ans = 0 
        
        for (x, _) in points: 
            if last < x: 
                last = x + w
                
                ans += 1 
                
        return ans 
        
        
