# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums) 
        
        seen = {num for num in nums}
        
        prefix = nums[0]
        
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                prefix += nums[i]
                
            else: 
                break 
                
        while prefix in nums: 
            prefix += 1 
            
        return prefix
