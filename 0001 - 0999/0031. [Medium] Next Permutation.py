# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
            
        def reverse(i):
            start = i
            end = n - 1
            while start < end: 
                swap(start, end)
                start += 1 
                end -= 1 
                
        n = len(nums)
        
        i = n - 2
        
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1 
        
        if i >= 0: 
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1 
                
            swap(i, j)
        
        reverse(i + 1)
        
        
        
        
        
