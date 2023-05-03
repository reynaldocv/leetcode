# https://leetcode.com/problems/arithmetic-slices/# 

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums) 
        
        prevRatio = inf 
        count = 0
        
        ans = 0
        
        for i in range(1, n):
            ratio = nums[i] - nums[i - 1]
            
            if prevRatio == ratio: 
                count += 1 
                ans += count 
                
            else: 
                prevRatio = ratio
                count = 0 
                
        return ans 
                
            
