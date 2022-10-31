# https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        stack = []
        
        for j in range(n):
            stack.append((0, j))
            
        for i in range(1, m):
            stack.append((i, 0))
            
        for (x, y) in stack: 
            value = matrix[x][y]
            
            while x < m and y < n:         
                if matrix[x][y] != value: 
                    return False 
                
                x += 1 
                y += 1
                            
        return True 
                
