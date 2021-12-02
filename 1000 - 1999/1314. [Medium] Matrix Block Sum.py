# https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        accMat = [[mat[i][j] for j in range(m)] for i in range(n)]        
        for i in range(n):
            for j in range(m):
                if i == 0 and j > 0: 
                    accMat[0][j] += accMat[0][j - 1]
                if j == 0 and i > 0: 
                    accMat[i][0] += accMat[i - 1][0]
                if i > 0 and j > 0: 
                    accMat[i][j] += accMat[i - 1][j] + accMat[i][j - 1] - accMat[i - 1][j - 1]
        
        ans = [[0 for j in range(m)] for i in range(n)]        
        for i in range(n):
            for j in range(m):
                x0, y0 = i - k - 1, j - k - 1
                x1, y1 = min(n - 1, i + k), min(m - 1, j + k)
                ans[i][j] = accMat[x1][y1]
                if x0 >= 0: 
                    ans[i][j] -= accMat[x0][y1]
                if y0 >= 0: 
                    ans[i][j] -= accMat[x1][y0]
                if x0 >= 0 and y0>= 0: 
                    ans[i][j] += accMat[x0][y0]
    
        return ans
                    
                
