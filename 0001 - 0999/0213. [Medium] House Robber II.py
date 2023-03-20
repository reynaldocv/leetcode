# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            dp = defaultdict(lambda: 0)
            
            ans = 0 
            
            for i in range(n - 1):
                dp[i] = arr[i] + max(dp[i - 2], dp[i - 3])
                
                ans = max(ans, dp[i])
                
            return ans 
        
        n = len(nums)
        
        if n == 1: 
            return nums[0]
        
        return max(helper(nums[: -1]), helper(nums[1: ]))
        
                
            
        
        
        
