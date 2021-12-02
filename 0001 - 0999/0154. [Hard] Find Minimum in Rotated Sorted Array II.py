# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0 
        end = n - 1
        
        while end - start > 0:
            m = (end + start)//2
            if nums[m] == nums[end]:
                end -= 1
            elif nums[m] > nums[end]:
                start = m + 1
            else: 
                end = m
                
        return nums[start]
        
        
