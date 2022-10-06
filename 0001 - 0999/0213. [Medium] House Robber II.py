# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            n = len(arr)
            
            dp = [num for num in arr]
            ans = 0 
            
            for i in range(n):
                val3 = dp[i - 3] if i - 3 >= 0 else 0 
                val2 = dp[i - 2] if i - 2 >= 0 else 0 
                
                dp[i] += max(val2, val3)
                ans = max(ans, dp[i])
                
            return ans 
        
        n = len(nums)
        
        if n == 1: 
            return nums[0]
        
        return max(helper(nums[: -1]), helper(nums[1: ]))
                
            
        
        
        
