# https://leetcode.com/problems/largest-triangle-area/

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        """
        :type points: List[List[int]]
        :rtype: float
        """
        ans = 0
        n = len(points)
        for i in range(n): 
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    l1 = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**.5
                    l2 = ((points[i][0] - points[k][0])**2 + (points[i][1] - points[k][1])**2)**.5
                    l3 = ((points[k][0] - points[j][0])**2 + (points[k][1] - points[j][1])**2)**.5
                    
                    s = (l1 + l2 + l3)/2
                    if s > l1 and s > l2 and s > l3:
                        area = (s*(s - l1)*(s - l2)*(s - l3))**.5
                        ans = max(ans, area)
        return ans
            
        
