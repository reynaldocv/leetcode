# https://leetcode.com/problems/modify-the-matrix/

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        
        maxElem = [-inf for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                maxElem[j] = max(maxElem[j], matrix[i][j])
                
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1: 
                    matrix[i][j] = maxElem[j]
                    
        return matrix
