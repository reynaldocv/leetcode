# https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def helper(hour1, hour2):
            seg1 = hour1[0]*60 + hour1[1]
            seg2 = hour2[0]*60 + hour2[1]
            diff = abs(seg2 - seg1)
            
            return min(diff, 24*60 - diff)
        
        n = len(timePoints)
        
        arr = [(int(hour[:2]), int(hour[3:])) for hour in timePoints]
        arr.sort()
        
        ans = helper(arr[0], arr[-1])
        
        for i in range(n - 1):
            ans = min(ans, helper(arr[i], arr[i + 1]))
        
        return ans
        
