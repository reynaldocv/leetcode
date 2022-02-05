# https://leetcode.com/problems/find-a-peak-element-ii/

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        ans = (-inf, -inf, -inf)
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(n):
                tmp = -inf if i == 0 else mat[i - 1][j]
                tmp = max(tmp, -inf if j == 0 else mat[i][j - 1])
                tmp = max(tmp, -inf if j == n - 1 else mat[i][j + 1])
                tmp = max(tmp, -inf if i == m - 1 else mat[i + 1][j])
                
                if tmp < mat[i][j]:
                    ans = max(ans, (mat[i][j], i, j))
                    
        return (ans[1], ans[2])
                
        
