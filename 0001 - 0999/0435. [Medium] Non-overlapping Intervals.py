# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:      
        n = len(intervals)        
        intervals.sort(key = lambda item: (item[0], -item[1]))
        (s0, e0) = intervals[0]
        i = 1      
        ans = 0
        while i < n: 
            (s1, e1) = intervals[i]
            sMax = max(s0, s1)
            eMin = min(e0, e1)            
            if sMax < eMin: 
                if e0 >= e1:                     
                    s0 = s1
                    e0 = e1                   
                ans += 1
            elif e0 < e1: 
                s0 = s1
                e0 = e1               
            i += 1
        
        return ans
                 
                    
                
