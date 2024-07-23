# https://leetcode.com/problems/minimum-sideway-jumps/

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles) 
        
        dp = defaultdict(lambda: [inf, 0, 0, 0])
        
        dp[0] = [inf, 1, 0, 1]
        
        for i in range(1, n):
            if obstacles[i] == 0:                             
                dp[i][1] = min(dp[i - 1][1], dp[i - 1][2] + 1, dp[i - 1][3] + 1)
                dp[i][2] = min(dp[i - 1][2], dp[i - 1][1] + 1, dp[i - 1][3] + 1)
                dp[i][3] = min(dp[i - 1][3], dp[i - 1][1] + 1, dp[i - 1][2] + 1)
                
            else: 
                j = obstacles[i]
                    
                dp[i][j] = inf 
                    
                for k in range(1, 4):
                    if k != j:
                        dp[i][k] = min(dp[i - 1][k], dp[i - 1][6 - k - j] + 1)
                        
        return min(dp[n - 1])
        
