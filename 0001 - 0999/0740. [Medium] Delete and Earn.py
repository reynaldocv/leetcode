# https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = 2*10**4
        dp = [0]*n
        
        for num in nums: 
            dp[num] += num
        
        ans = max(dp[0], dp[1])
        for i in range(2, n):
            val1 = dp[i - 2] if i - 2>= 0 else 0
            val2 = dp[i - 3] if i - 3>= 0 else 0
            dp[i] += max(val1, val2)
            ans = max(ans, dp[i])    
        
        return ans
        
            
        
