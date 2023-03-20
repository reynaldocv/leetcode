# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(value):
            start = -1 
            end = n
            
            while end - start > 1: 
                middle = (end + start)//2
                
                if nums[middle] < value: 
                    start = middle 
                    
                else: 
                    end = middle 
                    
            return end 
        
        n = len(nums)
        
        left = helper(target)
        
        if left >= n or nums[left] != target:
            return [-1, -1]
        
        right = helper(target + 1)
        
        return [left, right - 1]
        
        
