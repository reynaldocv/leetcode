# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) 
        if nums[0] > nums[n - 1]:            
            start = -1
            end = n - 1 
            while end - start > 1:
                m = (end + start)//2
                elemStart = nums[end]
                if nums[m] < elemStart:
                    end = m 
                else: 
                    start = m 

            if nums[0] <= target <= nums[end - 1]:
                start = 0 
            else: 
                start = end
                end = n
        else: 
            start = 0 
            end = n        
       
        while end - start > 1:
            m = (end + start)//2
            if nums[m] <= target:
                start = m 
            else: 
                end = m
        
        return -1 if nums[start] != target else start
