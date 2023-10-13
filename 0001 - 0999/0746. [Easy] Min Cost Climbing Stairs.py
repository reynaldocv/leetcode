# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        dp = [num for num in cost]
        
        for i in range(2, n):
            dp[i] += min(dp[i - 1], dp[i - 2])
            
        return min(dp[-1], dp[-2])
            
        
