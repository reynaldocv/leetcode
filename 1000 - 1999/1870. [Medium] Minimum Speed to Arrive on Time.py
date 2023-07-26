# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def helper(speed):
            time = 0 
            
            for num in dist[: -1]: 
                time += ceil(num/speed)
                
            time += dist[-1]/speed
            
            return time <= hour
        
        n = len(dist)
        
        if hour <= n - 1:
            return -1 
        
        start = 0
        end = 10**9 + 1
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if helper(middle):
                end = middle 
            
            else: 
                start = middle 
                
        return end 
                
