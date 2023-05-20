# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0]) 
        
        columns = set()
        rows = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: 
                    columns.add(j)
                    rows.add(i)
                    
        for i in range(m):
            for j in range(n):
                if i in rows or j in columns: 
                    matrix[i][j] = 0 
                    
                    
                    
                    
