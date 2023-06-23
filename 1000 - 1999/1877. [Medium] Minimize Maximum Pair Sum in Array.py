# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums.sort() 
        
        ans = 0 
        
        for i in range(n//2):
            ans = max(ans, nums[i] + nums[n - 1 - i])
            
        return ans 
        
