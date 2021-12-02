# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowsZero = {}
        colsZero = {}
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0: 
                    rowsZero[i] = True
                    colsZero[j] = True
                    
        for i in range(n):
            if i in rowsZero: 
                for j in range(m):
                    matrix[i][j] = 0
        
        for j in range(m):
            if j in colsZero: 
                for i in range(n):
                    matrix[i][j] = 0
                    
                    
