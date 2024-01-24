# https://leetcode.com/problems/wiggle-sort-ii/

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.        
        
        """
        n = len(nums)
        
        arr = sorted(nums, key = lambda item: -item) 
        
        minor = n//2
        maior = 0
        
        for i in range(n):
            if i % 2 == 0: 
                nums[i] = arr[minor]                
                minor += 1
                
            else: 
                nums[i] = arr[maior]                
                maior += 1 
