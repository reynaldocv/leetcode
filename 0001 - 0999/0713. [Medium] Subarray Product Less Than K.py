# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: 
            return 0 
        
        prefix = 1
        cnt = 0
        ans = 0
        
        idx = 0 
        
        for (i, num) in enumerate(nums): 
            prefix *= num
            cnt += 1 
                
            while prefix >= k: 
                prefix //= nums[idx]
                idx += 1 
                cnt -= 1 
                
            ans += cnt
        
        return ans 

