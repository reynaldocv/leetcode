# https://leetcode.com/problems/count-servers-that-communicate/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        cntRows = defaultdict(lambda: 0)
        cntCols = defaultdict(lambda: 0)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    cntRows[i] += 1 
                    cntCols[j] += 1 
                    
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    if cntCols[j] > 1 or cntRows[i] > 1: 
                        ans += 1 
                        
        return ans 
