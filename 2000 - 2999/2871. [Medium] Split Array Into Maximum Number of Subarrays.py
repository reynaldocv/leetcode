# https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        ans = 0
        
        prefix = -1
        
        for x in nums: 
            prefix &= x 
            
            if prefix == 0: 
                ans += 1
                
                prefix = -1
        
        return max(1, ans)
        
