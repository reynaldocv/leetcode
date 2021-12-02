# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]        
        
        ans = 0        
        aux = 1
        for i in range(n):
            if nums[i] == 0:                   
                aux = 1
            else: 
                aux *= nums[i]
                ans = max(ans, aux)
        
        nums = nums[::-1]
        aux = 1
        for i in range(n):
            if nums[i] == 0:                   
                aux = 1
            else: 
                aux *= nums[i]
                ans = max(ans, aux)
        
        return ans
        
