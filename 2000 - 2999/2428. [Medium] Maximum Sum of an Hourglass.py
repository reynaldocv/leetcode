# https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + grid[i - 1][j - 1]
                
        ans = 0 
        
        for i in range(3, m + 1):
            for j in range(3, n + 1):
                tmp = dp[i][j] - dp[i - 3][j] - dp[i][j - 3] + dp[i - 3][j - 3] - grid[i - 2][j - 1] - grid[i - 2][j - 3]
                
                ans = max(ans, tmp)
                
        return ans 
