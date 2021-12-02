# https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        ans = 0
        for i in range(1, l):
            x = points[i][0] - points[i-1][0]
            y = points[i][1] - points[i-1][1]
            ans += max(abs(x), abs(y))
        return ans
