# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0: return [-1, -1]
        start = -1
        end = n - 1
        ans = [-1, -1]        
        while end - start > 1:
            m = (end + start)//2
            if nums[m] < target:
                start = m 
            else: 
                end = m        
       
        if nums[end] != target: 
            return ans
        else: 
            ans[0] = end
            start = end
            end = n
            while end  - start > 1: 
                m = (end + start)//2
                if nums[m] <= target:
                    start = m 
                else: 
                    end = m     
            ans[1] = start
            return ans
