# https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angleMinutes = (minutes/60*360) % 360
        angleHour = ((hour/12*360)%360 + 30*(minutes/60))% 360
        
        ans = abs(angleHour - angleMinutes)
        
        return min(ans, 360 - ans)
        
        
