# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = [[0 for i in range(m)] for j in range(n)]
        for (row, col) in indices:
            for c in range(m):
                matrix[row][c] += 1
            for r in range(n):
                matrix[r][col] += 1
        ans = 0
        for col in range(m):
            for row in range(n):
                if (matrix[row][col] % 2 == 1):
                    ans = ans + 1
                
        return ans
        
