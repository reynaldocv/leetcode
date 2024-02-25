# https://leetcode.com/problems/type-of-triangle/

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        
        if not(nums[1] - nums[0] < nums[2] < nums[0] + nums[1]):
            return "none"
        
        arr = set(nums)
        
        n = len(arr)
        
        if n == 1: 
            return "equilateral"
        
        elif n == 2: 
            return "isosceles"
        
        else: 
            return "scalene"
        
        
