# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        sumRows = []
        sumCols = []
        
        for i in range(m):
            tmp = 0 
            
            for j in range(n):
                tmp += mat[i][j]
                
            sumRows.append(tmp)
            
        for j in range(n):
            tmp = 0 
            
            for i in range(m):
                tmp += mat[i][j]
                
            sumCols.append(tmp)
            
        ans = 0    
     
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and sumRows[i] == 1 and sumCols[j] == 1: 
                    ans += 1 
                    
        return ans 
