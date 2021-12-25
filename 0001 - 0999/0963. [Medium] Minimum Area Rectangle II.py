# https://leetcode.com/problems/minimum-area-rectangle-ii/

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        @cache
        def distance(x0, y0, x1, y1):
            return (x0 - x1)**2 + (y0 - y1)**2
        
        ans = inf
        
        for points in combinations(points, 4):
            val1 = distance(*points[0], *points[1])
            
            if val1 == distance (*points[2], *points[3]):
                val2 = distance(*points[0], *points[2])      
                
                if val2 == distance (*points[1], *points[3]):
                    val3 = distance(*points[0], *points[3])                        
                    
                    if val3 == distance(*points[1], *points[2]):
                        dist = [val1, val2, val3]
                
                        dist.sort()
                        ans = min(ans, (dist[0]*dist[1])**.5)

        return 0 if ans == inf else ans
            
                    
            

