# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        ans = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + grid[i - 1][j - 1]
                
                if dp[i][j] <= k: 
                    ans += 1 
                
                else: 
                    break 
        
        return ans 
