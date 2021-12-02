# https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        ans = 0        
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])       
                if matrix[i][j] == 1: 
                    ans = 1
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:  
                    matrix[i][j] = min(matrix[i - 1][j],matrix[i][j - 1],matrix[i - 1][j - 1]) + 1
                    ans = max(ans, matrix[i][j]) 
            
        return ans**2
