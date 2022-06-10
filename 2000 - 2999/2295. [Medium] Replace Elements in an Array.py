# https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index = {}
        
        for (i, num) in enumerate(nums):
            index[num] = i 
            
        for (a, b) in operations: 
            idx = index.pop(a)
            index[b] = idx
            
        for key in index: 
            nums[index[key]] = key
            
        return nums    
        
            
