# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        start = 0 
        end = n 
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if nums[0] <= nums[middle]:
                start = middle 
                
            else: 
                end = middle 
                
        if end == n: 
            return nums[0]
        
        else: 
            return nums[end]
        
        
        
            
        
        
