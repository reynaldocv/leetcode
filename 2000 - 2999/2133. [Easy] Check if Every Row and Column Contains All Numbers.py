# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:               
        n = len(matrix)
        p = [i for i in range(1, n + 1)]
        
        for row in matrix: 
            if sorted(row) != p:
                return False
            
        tMatrix = [[matrix[i][j] for i in range(n)] for j in range(n)]
        
        for row in tMatrix: 
            if sorted(row) != p:
                return False
        
        return True
        
