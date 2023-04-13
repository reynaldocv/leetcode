# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for j in range(n)] for i in range(m)]
        
        for (row, col) in indices:
            for j in range(n):
                matrix[row][j] += 1
                
            for i in range(m):
                matrix[i][col] += 1
                
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if (matrix[i][j] % 2 == 1):
                    ans = ans + 1
                
        return ans
        
