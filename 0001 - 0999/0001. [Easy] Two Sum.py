# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for (i, num) in enumerate(nums):
            tmp = target - num 
            
            if tmp in seen: 
                return [seen[tmp], i]
            
            seen[num] = i 
            
        
        
