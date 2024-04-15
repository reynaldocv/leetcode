# https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        @cache
        def helper(idx, ith, mask):
            if idx == n and ith == m: 
                return 0 
            
            elif idx == n or ith == m:  
                return inf 
            
            else: 
                mask = mask & nums[idx]
                
                if mask < andValues[ith]:
                    return inf
                
                if mask == andValues[ith]:
                    return min(nums[idx] + helper(idx + 1, ith + 1, -1), helper(idx + 1, ith, mask))
                
                return helper(idx + 1, ith, mask)                
                
        n = len(nums)
        m = len(andValues)
        
        return -1 if helper(0, 0, -1) == inf else helper(0, 0, -1)
