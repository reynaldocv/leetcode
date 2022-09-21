# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        start = -1 
        end = n
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if nums[mid] < target: 
                start = mid 
            else: 
                end = mid 
                
        return end 
        
