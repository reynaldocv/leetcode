# https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) 
        
        nums.sort() 
        
        idx = bisect_left(nums, target)
        
        ans = []
        
        while idx < n and nums[idx] == target: 
            ans.append(idx)
            
            idx += 1 
            
        return ans 
        
        
