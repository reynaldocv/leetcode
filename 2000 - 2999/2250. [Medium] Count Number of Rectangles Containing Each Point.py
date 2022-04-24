# https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        n = len(points)
        
        ans = [0 for _ in range(n)]
        
        rects = [[] for i in range(101)]
        
        for (x, y) in rectangles:
            insort(rects[y], x)
        
        for (i, (x, y)) in enumerate(points):
            cnt = 0
            
            for j in range(y, 101):
                if rects[j]:
                    idx = bisect_left(rects[j], x)
                    cnt += len(rects[j]) - idx 
                    
            ans[i] = cnt
            
        return ans
