# https://leetcode.com/problems/maximum-width-ramp/

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        arr = [(num, i) for (i,num) in enumerate(nums)]
        arr.sort()
        
        ans = 0 
        
        minIdx = arr[0][1]
        
        for (nums, i) in arr:
            ans = max(ans, i - minIdx)
            minIdx = min(minIdx, i)
        
        return ans
        
