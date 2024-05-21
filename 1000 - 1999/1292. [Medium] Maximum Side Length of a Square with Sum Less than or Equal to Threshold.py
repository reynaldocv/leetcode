# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]
                
        ans = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(ans, min(i, j) + 1):
                    x0, y0 = i - k, j - k 
                    
                    tmp = dp[i][j] - dp[x0][j] - dp[i][y0] + dp[x0][y0]
                    
                    if tmp <= threshold:
                        ans += 1 
                        
                    else:
                        break
                        
        return ans - 1
                    
                
        
                
        
