# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: 0)
        
        n = len(nums)
        
        ans = 0 
        
        for i in range(n):
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
            
            ans = max(ans, dp[i])
            
        return ans 
            
        
