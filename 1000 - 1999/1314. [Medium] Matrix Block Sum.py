# https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]
                
        ans = [[0 for _ in range(n)] for _ in range(m)]
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                maxI = i + k if i + k < m else m
                minI = i - k - 1 if i - k - 1 > 0 else 0 
                
                maxJ = j + k if j + k < n else n
                minJ = j - k - 1 if j - k - 1 > 0 else 0 
                
                ans[i - 1][j - 1] = dp[maxI][maxJ] - dp[minI][maxJ] - dp[maxI][minJ] + dp[minI][minJ]
                
        return ans 
                 
                
                    
                
