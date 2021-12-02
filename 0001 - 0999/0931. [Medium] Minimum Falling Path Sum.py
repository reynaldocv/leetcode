# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        for i in range(1, n):
            for j in range(m):
                val1 = matrix[i - 1][j - 1] if 0 <= j - 1 else inf 
                val2 = matrix[i - 1][j] 
                val3 = matrix[i - 1][j + 1] if j + 1 < n else inf
                
                matrix[i][j] += min(val1, val2, val3)
                
        return min(matrix[-1])
        
