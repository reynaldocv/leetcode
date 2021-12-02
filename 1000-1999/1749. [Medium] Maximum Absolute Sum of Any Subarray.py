# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [num for num in nums]
        
        ans = abs(nums[0])
        for i in range(1, n):
            arr[i] += max(0, arr[i - 1])
            ans = max(ans, arr[i])
        
        arr = [-num for num in nums]
        
        for i in range(1, n):
            arr[i] += max(0, arr[i - 1])
            ans = max(ans, arr[i])
        
        return ans
