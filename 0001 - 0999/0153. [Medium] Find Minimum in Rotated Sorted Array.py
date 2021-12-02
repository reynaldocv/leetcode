# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]
        
        start = 0 
        end = n 
        ans = nums[start]
        while end - start > 1: 
            m = (end + start)//2
            if nums[start] < nums[m]:
                ans = min(ans, nums[start])
                start = m
            else: 
                ans = min(ans, nums[m])
                end = m 
        
        return ans
                
            
        
        
