# https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        n = len(points)
        
        rects = [[] for i in range(101)]
        
        for (x, y) in rectangles:
            insort(rects[y], x)
        
        ans = []
        
        for (x, y) in points:
            cnt = 0
            
            for i in range(y, 101):
                if rects[i]:
                    idx = bisect_left(rects[i], x)
                    cnt += len(rects[i]) - idx 
                    
            ans.append(cnt)
            
        return ans
            
