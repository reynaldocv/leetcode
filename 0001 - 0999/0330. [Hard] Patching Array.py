# https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = prefix = k = 0 
        while prefix < n: 
            if k < len(nums) and nums[k] <= prefix + 1: 
                prefix += nums[k]
                k += 1
            else: 
                ans += 1
                prefix += prefix + 1
        return ans 
        
