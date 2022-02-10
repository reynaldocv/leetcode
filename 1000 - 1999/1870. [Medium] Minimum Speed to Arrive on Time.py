# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def helper(speed):
            ans = 0 
            for d in dist[:-1]:
                ans += ceil(d/speed)
            
            ans += dist[-1]/speed
            
            return ans

        start = 0 
        end = 10**7
        
        if helper(end) > hour: 
            return -1
        
        while end - start > 1: 
            m = (end + start)//2
            if helper(m) > hour: 
                start = m
            else: 
                end = m 
                
        return end
