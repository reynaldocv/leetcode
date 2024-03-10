https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums) 
        
        left = 0         
        right = sum(nums)
        
        ans = 0 
        
        for i in range(n - 1): 
            left += nums[i] 
            right -= nums[i]
            
            if left >= right: 
                ans += 1 
                
        return ans 
            
            
