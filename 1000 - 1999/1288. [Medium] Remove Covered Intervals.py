# https://leetcode.com/problems/remove-covered-intervals/

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda item: (item[0], -item[1]))
        
        (a, b) = intervals[0]
        ans = len(intervals)
        
        for (c, d) in intervals[1:]:
            if a <= c and d <= b: 
                ans -= 1 
            else: 
                a, b = c, d
                
        return ans
