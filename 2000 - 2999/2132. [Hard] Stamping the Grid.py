# https://leetcode.com/problems/stamping-the-grid/

class Solution:
    def possibleToStamp(self, grid: List[List[int]], h: int, w: int) -> bool:
        m, n = len(grid), len(grid[0])

        aSum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                aSum[i + 1][j + 1] = aSum[i][j + 1] + aSum[i + 1][j] - aSum[i][j] + grid[i][j]

        stamp = [[False for _ in range(n)] for _ in range(m)]
        
        for i in range(m - h + 1):
            for j in range(n - w + 1):
                stamp[i][j] = aSum[i][j] + aSum[i + h][j + w] - aSum[i][j + w] - aSum[i + h][j] == 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    flag = False
                    
                    for ii in range(i, max(-1, i - h), -1):
                        if flag: 
                            break
                            
                        for jj in range(j, max(-1, j - w), -1):
                            if stamp[ii][jj]:
                                for s in range(ii, ii + h):
                                    for t in range(jj, jj + w):
                                        grid[s][t] = 1  # skip them later
                                flag = True
                                break
                    if not flag: 
                        return False
        
        return True
                
        
        
            
     
        
        
