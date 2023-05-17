# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        start = 0 
        end = n 
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if nums[middle - 1] < nums[middle]:
                start = middle 
                
            else: 
                end = middle 
                
        return start
        
        
