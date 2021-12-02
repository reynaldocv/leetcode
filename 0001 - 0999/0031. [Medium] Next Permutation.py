# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = -1
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                idx = i - 1
                break        
        if idx == -1: 
            nums[:] = nums[::-1]    
        
        min_ = (nums[idx + 1] - nums[idx], idx + 1)        
        for j in range(idx + 2, n):
            if nums[j] - nums[idx] > 0:
                min_ = min(min_, (nums[j] - nums[idx], j))
        nums[min_[1]] ,nums[idx] = nums[idx], nums[min_[1]]
        
        nums[idx + 1:] = sorted(nums[idx + 1:])
        
        
        
        
        
