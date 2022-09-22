# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        idx = 0 
        
        for num in nums: 
            if num != 0: 
                nums[idx] = num 
                idx += 1 
                
        for i in range(idx, n):
            nums[i] = 0
        
