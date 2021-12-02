# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        def helper(a, b):
            distance = b - a + 1
            if dp[a][b] != 0 or distance < 3: 
                return dp[a][b]
            
            ans = inf            
            for i in range(a + 1, b):
                ans = min(ans, values[a]*values[i]*values[b] + helper(a, i) + helper(i, b))
            
            dp[a][b] = ans
            return dp[a][b]
        
        n = len(values) 
        dp = [[0]*50 for _ in range(50)]
        
        return helper(0, n- 1)
            
        
            
            
        
            
            
            
            
            
            
