# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for i in range(1, n):
            for j in range(n):
                left = matrix[i - 1][j - 1] if j - 1 >= 0 else inf 
                right = matrix[i - 1][j + 1] if j + 1 < n else inf 
                
                value = matrix[i - 1][j]
                
                matrix[i][j] += min(left, value, right)
                
        return min(matrix[-1])
                
                
        
