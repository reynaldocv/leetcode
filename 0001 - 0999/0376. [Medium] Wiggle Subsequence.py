# https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums) 
         
        negative = 1
        positive = 1
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] > 0: 
                positive = negative + 1
                
            elif nums[i] - nums[i - 1] < 0:
                negative = positive + 1
                
        return max(negative, positive)
        
        
