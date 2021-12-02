# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def distance(point0, point1):
            return ((point0[0] - point1[0])**2 + (point0[1] - point1[1])**2)**.5
        
        ans = [0]*len(queries)
        for i in range(len(queries)): 
            (x0, y0, r) = queries[i]
            for point in points: 
                if distance((x0, y0), point) <= r: 
                    ans[i] += 1
        
        return ans
                
                
        
        
        
