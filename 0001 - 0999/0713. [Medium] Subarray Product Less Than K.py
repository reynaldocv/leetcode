# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt = 0 
        prev = 1 
        
        start = 0 
        
        ans = 0 
        
        for (i, num) in enumerate(nums): 
            prev *= num
            cnt += 1 
            while start <= i and prev >= k: 
                prev //= nums[start]
                
                start += 1 
                cnt -= 1 
                
            ans += cnt 
            
        return ans 
                
