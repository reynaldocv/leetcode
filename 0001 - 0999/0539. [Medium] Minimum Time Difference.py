# https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def helper(word):
            return 60*int(word[: 2])  + int(word[3: ])
        
        n = len(timePoints) 
        
        timePoints.sort(key = lambda item: helper(item))
        
        ans = 60*24 - helper(timePoints[-1]) + helper(timePoints[0])
        
        for i in range(n - 1):
            ans = min(ans, helper(timePoints[i + 1]) - helper(timePoints[i]))
        
        return ans 
        
        
        
