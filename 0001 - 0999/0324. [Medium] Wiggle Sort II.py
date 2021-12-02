# https://leetcode.com/problems/wiggle-sort-ii/

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = sorted(nums, reverse=True)
        
        middle = n//2 if n % 2 == 0 else n//2 + 1
        
        j = 0
        
        for i in range(1, n, 2):
            nums[i] = temp[j]
            j += 1
            if j == middle:
                break
                
        for i in range(0, n, 2):
            nums[i] = temp[j]
            j += 1
            if j == len(nums):
                break
        
