# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        
        arr = sorted(nums)
        
        for i in range(n):             
            if arr == nums[i: ] + nums[: i]:
                return True 
            
        return False 
