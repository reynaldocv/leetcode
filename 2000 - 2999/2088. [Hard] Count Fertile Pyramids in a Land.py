# https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        def helper(vals):
            ans = 0 
            for j in range(m):
                width = 0 
                for i in range(n):
                    if vals[i][j] > 0: 
                        width = min(width + 1, vals[i][j])
                    else: 
                        width = 0
                    ans += max(0, width - 1)
                        
            return ans 
                       
        n, m = len(grid), len(grid[0])
        vals =  [[inf for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0: 
                    vals[i][j] = 0

                elif j == 0: 
                    vals[i][j] = 1

                else: 
                    vals[i][j] = min(vals[i][j], 1 + vals[i][j - 1])

                if grid[i][~j] == 0: 
                    vals[i][~j] = 0

                elif j == 0: 
                    vals[i][~j] = 1

                else: 
                    vals[i][~j] = min(vals[i][~j], 1 + vals[i][~j + 1])

        return helper(vals) + helper(vals[:: -1])
                        
        
                
            
