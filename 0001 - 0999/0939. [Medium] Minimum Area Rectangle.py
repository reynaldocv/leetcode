# https://leetcode.com/problems/minimum-area-rectangle/

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = defaultdict(lambda: False)
        
        for (x, y) in points:             
            seen[(x, y)] = True
            
        ans = inf
        for (x1, y1) in points:
            for (x2, y2) in points: 
                if x1 != x2 and y1 != y2:
                    if seen[(x1, y2)] and seen[(x2, y1)]:
                        ans = min(ans, abs((x2 - x1)*(y2 - y1)))
                        
        return 0 if ans == inf else ans
                    
                    
                    
                    
        
