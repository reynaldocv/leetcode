# https://leetcode.com/problems/remove-covered-intervals/

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        ans = [intervals[0]]
        
        for (s, e) in intervals[1:]: 
            (s0, e0) = ans[-1]
            if s0 == s: 
                ans.pop()
                ans.append((s, e))        
                
            elif e0 >= e:
                continue
                
            else: 
                ans.append((s, e))
                
        return len(ans)
                
