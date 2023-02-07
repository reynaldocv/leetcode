# https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if n == 1: 
            return True
        
        asc = desc = True
        
        for i in range(0, n - 1):
            if nums[i] < nums[i + 1]:
                asc = False
                break
                
              
                
        for i in range(0, n - 1):
            if nums[i] > nums[i + 1]:
                desc = False
                break
                
        return (asc or desc)
        
 
