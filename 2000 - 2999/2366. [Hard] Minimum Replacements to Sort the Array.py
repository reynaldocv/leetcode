# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums) 
        
        ans = 0 
        
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
                
            else: 
                nElems = (nums[i] + nums[i + 1] - 1)//nums[i + 1]
                
                ans += nElems - 1
                
                nums[i] = nums[i]//nElems
                
        return ans 
        
