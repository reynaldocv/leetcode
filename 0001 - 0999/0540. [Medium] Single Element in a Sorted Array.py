# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        start = 0 
        end = n
        
        while end - start > 1: 
            mid = (end + start)//2            
            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    start = mid  
                else: 
                    end = mid 
            elif nums[mid] == nums[mid - 1]:
                end = mid 
            else: 
                start = mid 
            
        return nums[start]
                
            
        
        
