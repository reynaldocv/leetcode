# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        start = -1 
        end = n - 1
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if nums[mid] < target :
                start = mid 
            else: 
                end = mid 
                
        return end if nums[end] == target else -1
        
