# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, lastHigh = 0, 0
        
        for i in range(len(gain)):   
            lastHigh += gain[i]
            ans = max(ans, lastHigh)
            
        return ans
        
