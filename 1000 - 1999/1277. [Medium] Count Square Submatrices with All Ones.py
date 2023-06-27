# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        tmp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        ans = 0 
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 1: 
                    minElem = min(tmp[i - 1][j], tmp[i][j - 1], tmp[i - 1][j - 1])
                    
                    tmp[i][j] = minElem + 1
                    
                    ans += tmp[i][j]
                    
        return ans 
            
            
