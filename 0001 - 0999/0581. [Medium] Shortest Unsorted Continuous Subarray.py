# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums) 
        arr = sorted(nums)
        
        start, end = -1, -1 
        
        for i in range(n):
            if nums[i] != arr[i]:
                if start == -1:
                    start = i 
                    
                end = i 
                
        if end == -1: 
            return 0 
        
        return end - start + 1
        
