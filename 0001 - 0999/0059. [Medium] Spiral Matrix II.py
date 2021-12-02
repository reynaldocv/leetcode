# https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[False for i in range(n)] for j in range(n)]
        direction = [(0,1), (1, 0), (0, -1), (-1, 0)]
        k = 0 
        x, y = 0, 0 
        value = 1 
        while value <= n*n: 
            if x < n and y < n and matrix[x][y] == False: 
                matrix[x][y] = value
                value += 1
            else:
                x -= direction[k][0]
                y -= direction[k][1]
                k = (k + 1) % 4
            x += direction[k][0]
            y += direction[k][1]
        
        return matrix
                
                
        
        
