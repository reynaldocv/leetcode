# https://leetcode.com/problems/largest-triangle-area/

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        
        ans = 0
        
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    (x1, y1) = points[i]
                    (x2, y2) = points[j]
                    (x3, y3) = points[k]
                    
                    a = ((y2 - y1)**2 + (x2 - x1)**2)**.5
                    b = ((y3 - y1)**2 + (x3 - x1)**2)**.5
                    c = ((y3 - y2)**2 + (x3 - x2)**2)**.5
                    
                    s = (a + b + c)/2
                    
                    if s >= max(a, b, c):                    
                        ans = max(ans, (s*(s - a)*(s - b)*(s - c))**.5)
                    
        return ans
            
        
