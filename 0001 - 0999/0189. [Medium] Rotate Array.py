# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def inverse(arr, start, end):            
            while end > start:
                arr[start], arr[end] = arr[end], arr[start]
                end -= 1
                start += 1
            
        n = len(nums)
        k = k % n
        inverse(nums, 0, n - 1)
        inverse(nums, 0, k - 1)
        inverse(nums, k, n - 1)
        
            
