# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = sorted(nums)
        
        n = len(nums)
        start = 0 
        end = n - 1
        
        while start < n and arr[start] == nums[start]:
            start += 1
            
        if start == n: 
            return 0
        
        while arr[end] == nums[end]:
            end -= 1
            
        return end - start + 1
        
