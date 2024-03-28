# https://leetcode.com/problems/minimum-area-rectangle/

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = {(x, y) for (x, y) in points}
        
        n = len(points)
        
        ans = inf 
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                (x0, y0) = points[i]
                (x1, y1) = points[j]
                
                if (x0, y1) in seen and (x1, y0) in seen:                     
                    dX = abs(x1 - x0)
                    dY = abs(y1 - y0)
                    
                    if dX*dY > 0:                     
                        ans = min(ans, dX*dY)
        
        return 0 if ans == inf else ans 
            
        
                    
                    
        
