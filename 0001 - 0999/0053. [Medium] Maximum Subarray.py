# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        prefix = 0 
        
        for num in nums: 
            prefix += num 
            
            ans = max(ans, prefix)
            
            if prefix < 0: 
                prefix = 0 
                
        return ans 
        
            
            
        
