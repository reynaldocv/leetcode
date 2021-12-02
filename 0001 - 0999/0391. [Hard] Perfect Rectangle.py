# https://leetcode.com/problems/perfect-rectangle/

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:        
        area = 0
        corner = set()
        r0 = s0 = inf
        r1 = s1 = -inf
        for (x0, y0, x1, y1) in rectangles: 
            area += (x1 - x0)*(y1 - y0)
            r0 = min(r0, x0)
            s0 = min(s0, y0)
            r1 = max(r1, x1)
            s1 = max(s1, y1)
            
            corner ^= {(x0, y0), (x0, y1), (x1, y0), (x1, y1)}
            
        return area == (r1 - r0)*(s1 - s0) and corner == {(r0, s0), (r0, s1), (r1, s0), (r1, s1)}
