# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(val):
            start = -1 
            end = n
            
            while end - start > 1: 
                mid = (end + start)//2
                if nums[mid] < val: 
                    start = mid
                else: 
                    end = mid
            
            return end 
        
        n = len(nums)
        if n == 0: 
            return [-1, -1]
        
        if target < nums[0] or nums[-1] < target: 
            return [-1, -1]
        
        idx = helper(target)
        if nums[idx] == target: 
            idx2 = helper(target + 1)
            return [idx, idx2 - 1]
        else: 
            return [-1, -1]
        
