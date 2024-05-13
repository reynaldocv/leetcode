# https://leetcode.com/problems/maximum-difference-score-in-a-grid/

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]                              

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(grid[i][j], dp[i + 1][j], dp[i][j + 1])
         
        ans = -inf

        for i in range(m):
            for j in range(n):
                if i + 1 < m:
                    ans = max(ans, dp[i + 1][j] - grid[i][j])
                    
                if j + 1 < n: 
                    ans = max(ans, dp[i][j + 1] - grid[i][j])

        return  ans
