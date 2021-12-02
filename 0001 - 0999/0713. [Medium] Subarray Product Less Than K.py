# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:        
        n = len(nums)
        left = 0 
        mult = 1
        ans = 0
        
        if k <= 0: 
            return 0
        
        for i in range(n):
            mult *= nums[i]
            while mult >= k and left < i: 
                mult //= nums[left]
                left += 1       
            if mult < k:
                ans += i - left + 1
        
        return ans

