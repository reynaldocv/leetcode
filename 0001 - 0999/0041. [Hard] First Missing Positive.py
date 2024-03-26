# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for (i, num) in enumerate(nums):
            if num <= 0: 
                nums[i] = n + 2
                
        for num in nums: 
            value = abs(num)
            
            if 0 < value <= n: 
                nums[value - 1] = -abs(nums[value - 1])
                
        for (i, num) in enumerate(nums): 
            if num > 0: 
                return i + 1
            
        return n + 1
        
        
