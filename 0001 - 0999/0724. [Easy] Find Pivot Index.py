# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = 0 
        suffix = sum(nums)
        
        for (i, num) in enumerate(nums):
            suffix -= num 
            
            if prefix == suffix: 
                return i 
            
            prefix += num 
            
        return -1
        

        
