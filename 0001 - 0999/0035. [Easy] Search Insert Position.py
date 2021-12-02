# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0 
        j = len(nums)
        if target <= nums[0]: return 0
        if target > nums[j - 1]: return j
        
        while (j - i > 1):
            m = (i + j)//2
            if nums[m] >= target:
                j = m
            else: 
                i = m        
        return j
            
