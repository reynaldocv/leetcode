# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        
        return nums[l-1]*nums[l-2] - nums[0]*nums[1]
