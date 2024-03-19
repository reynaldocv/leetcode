# https://leetcode.com/problems/max-points-on-a-line/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def helper(x0, y0, x1, y1):
            if x0 != x1 and y0 != y1: 
                dX = x1 - x0 
                dY = y1 - y0 
                
                common = gcd(dX, dY)
                
                dX //= common
                dY //= common
                
            elif x0 == x1:
                dY = 0 
                dX = 1                
                
            else: 
                dX = 0 
                dY = 1
                
            return (dX, dY)
        
        counter = defaultdict(lambda: defaultdict(lambda: 0))
        
        n = len(points)
        
        ans = 0 
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                (x0, y0) = points[i]
                (x1, y1) = points[j]
                
                (dX, dY) = helper(x0, y0, x1, y1)
                
                counter[(x0, y0)][(dX, dY)] += 1
                counter[(x1, y1)][(-dX, -dY)] += 1
                
                ans = max(ans, counter[(x0, y0)][(dX, dY)], counter[(x1, y1)][(-dX, -dY)])
                
        return ans + 1
                
