# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) 
        
        dpX = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dpY = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dpX[i][j] = dpX[i - 1][j] + dpX[i][j - 1] - dpX[i - 1][j - 1]
                dpY[i][j] = dpY[i - 1][j] + dpY[i][j - 1] - dpY[i - 1][j - 1]
                            
                if grid[i - 1][j - 1] == "X":
                    dpX[i][j] += 1
                    
                elif grid[i - 1][j - 1] == "Y":
                    dpY[i][j] += 1
                   
        ans = 0 
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if dpX[i][j] != 0 and dpX[i][j] == dpY[i][j]:
                    ans += 1 
                    
        return ans 
