# https://leetcode.com/problems/teemo-attacking/

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries) 
        
        ans = 0 
        
        for (i, time) in enumerate(timeSeries): 
            if i < n - 1: 
                ans += min(timeSeries[i + 1] - time, duration)
                
            else: 
                ans += duration
                
        return ans 
            
