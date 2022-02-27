# https://leetcode.com/problems/minimum-time-to-complete-trips/

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def helper(t):
            ans = 0 
            for num in time:
                ans += t//num
                
            return ans
        
        start = 0 
        end = max(time)*totalTrips + 1
        
        while end - start > 1: 
            m = (end + start)//2
            if helper(m) < totalTrips: 
                start = m 
            else: 
                end = m 
                
        return end
