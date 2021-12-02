# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        sum_ = sum(nums)
        l = len(nums)
        aux = 0
        for i in range(l):
            aux += nums[i]
            if aux > sum_ - aux:
                return nums[:i + 1]
        
        
        
