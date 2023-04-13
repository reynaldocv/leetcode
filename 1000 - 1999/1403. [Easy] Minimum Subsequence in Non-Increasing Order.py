# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        aSum = sum(nums)
        
        nums.sort() 
        
        prev = 0 
        
        for (i, num) in enumerate(nums):
            prev += num
            aSum -= num 
            
            if prev >= aSum: 
                return nums[i: ][:: -1]
        
