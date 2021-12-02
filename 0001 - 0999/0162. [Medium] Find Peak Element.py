# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        while (start < end):
            m = (start + end)//2
            if nums[m] > nums[m + 1]:
                end = m 
            else: 
                start = m + 1
        
        return start
        
