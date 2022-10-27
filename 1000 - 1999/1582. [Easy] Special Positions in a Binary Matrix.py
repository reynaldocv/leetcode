# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        tmp1 = [[0 for j in range(n + 1)] for i in range(m + 1)]
        tmp2 = [[0 for j in range(n + 1)] for i in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                tmp1[i][j] = tmp1[i][j - 1] + mat[i - 1][j - 1]
                tmp2[i][j] = tmp2[i - 1][j] + mat[i - 1][j - 1]
                
        ans = 0 
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1: 
                    if tmp1[i + 1][n] == 1 and tmp2[m][j + 1] == 1: 
                        ans += 1 
                        
        return ans 
