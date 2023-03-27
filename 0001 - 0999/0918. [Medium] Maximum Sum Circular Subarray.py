# https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def helper(arr):
            ans = [-inf]
            aSum = 0 
            
            for num in arr: 
                aSum += num
                
                ans.append(max(aSum, ans[-1]))
                
            return ans 
        
        ans = -inf 
        
        prev = 0 
        
        for num in nums: 
            prev += num 
            
            ans = max(ans, prev)
            
            if prev < 0: 
                prev = 0 
                
        left = helper(nums)
        right = helper(nums[:: -1])[:: -1]
        
        n = len(nums)
         
        for i in range(n + 1):
            ans = max(ans, left[i] + right[i])
            
        return ans 
        
        
        
