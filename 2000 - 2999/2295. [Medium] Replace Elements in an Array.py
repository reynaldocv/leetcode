# https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index = {num: i for (i, num) in enumerate(nums)}
        
        for (old, new) in operations: 
            idx = index[old]            
            index.pop(old)
            
            nums[idx] = new
            
            index[new] = idx 
            
        return nums
        
            
