# https://leetcode.com/problems/teemo-attacking/

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = duration
        for i in range(1, len(timeSeries)):
            if timeSeries[i - 1] + duration - 1 >= timeSeries[i]:
                ans += timeSeries[i] - timeSeries[i - 1] 
            else: 
                ans += duration 
        return ans
        
