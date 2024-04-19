# https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        nums.sort() 
        
        start = n//2
        
        ans = inf 
        
        if nums[start] <= k: 
            cnt = 0
            
            while start < n and nums[start] < k: 
                cnt += k - nums[start]
                
                start += 1 
                
            ans = min(ans, cnt)
            
        end = n//2
                
        if nums[end] >= k: 
            cnt = 0 
            
            while end >= 0 and nums[end] > k: 
                cnt += nums[end] - k
                
                end -= 1 
                
            ans = min(ans, cnt)
            
        return ans 
            
                
