# https://leetcode.com/problems/maximum-building-height/

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        dp = [[x, y] for (x, y) in restrictions]
        
        dp.append([1, 0])
        dp.append([n, n - 1])
        
        dp.sort()
        
        n = len(dp)
        
        for i in range(n - 2, -1, -1): 
            dp[i][1] = min(dp[i][1], dp[i + 1][1] + dp[i + 1][0] - dp[i][0])
        
        ans = 0 
        
        for i in range(1, n): 
            dp[i][1] = min(dp[i][1], dp[i-1][1] + dp[i][0] - dp[i-1][0])
            
            ans = max(ans, (dp[i - 1][1] + dp[i][0] - dp[i - 1][0] + dp[i][1])//2)
            
        return ans 
        
