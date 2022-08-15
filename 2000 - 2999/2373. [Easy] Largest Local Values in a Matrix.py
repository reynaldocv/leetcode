# https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n  = len(grid), len(grid[0])
        
        ans = [[inf for _ in range(n - 2)] for _ in range(m - 2)]
        
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                tmp = grid[i][j]
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        tmp = max(tmp, grid[ii][jj])
                
                ans[i - 1][j - 1] = tmp 
                
        return ans 
            
