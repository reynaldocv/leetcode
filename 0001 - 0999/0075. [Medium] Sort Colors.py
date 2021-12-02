# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        counter = {0: 0, 1: 0, 2:  0}
        for num in nums: 
            counter[num] += 1
        
        k = 0
        for i in range(len(nums)):
            while counter[k] <= 0:                
                k += 1
            nums[i] = k
            counter[k] -= 1
        
        
            
