# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(1, l):
            nums[i] += nums[i - 1]
        return nums
