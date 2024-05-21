# https://leetcode.com/problems/maximum-width-ramp/

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        arr = [(num, ith) for (ith, num) in enumerate(nums)]        
        arr.sort()        
        
        ans = 0         
        minIdx = inf
        
        for (num, ith) in arr:
            ans = max(ans, ith - minIdx)
        
            minIdx = min(minIdx, ith)
            
        return ans
        
