# https://leetcode.com/problems/count-submatrices-with-all-ones/

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(1, n):
                if mat[i][j] == 1: 
                    mat[i][j] += mat[i][j - 1]
                    
        ans = 0 
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0: 
                    aux = inf
                    for k in range(i, m):
                        aux = min(aux, mat[k][j])
                        ans += aux
                        
        return ans
        
