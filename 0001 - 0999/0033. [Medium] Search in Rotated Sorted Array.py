# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        left = 0
        right = n 
        
        while right - left > 1: 
            middle = (right + left)//2
            
            if nums[0] <= nums[middle]:
                left = middle 
            
            else: 
                right = middle 
                
        if right == n: 
            start = -1 
            end = n - 1
            
        elif nums[0] <= target <= nums[left]:
            end = left
            start = -1
            
        else: 
            start = right - 1
            end = n - 1
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if nums[middle] < target:
                start = middle 
            
            else: 
                end = middle 
        
        return end if nums[end] == target else -1
            
        
            
        
