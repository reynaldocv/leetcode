# https://leetcode.com/problems/largest-1-bordered-square/

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        def helper(grid):
            p, q = len(grid), len(grid[0])
            ans = [[grid[i][j] for j in range(q)] for i in range(p)]
            for i in range(p):
                prev = 0
                for j in range(q):
                    ans[i][j] += prev if ans[i][j] == 1 else 0 
                    prev = prev + 1 if ans[i][j] > 0 else 0
                        
            return ans
        
        n, m = len(grid), len(grid[0])
        tGrid = [[grid[i][j] for i in range(n)] for j in range(m)]        
        
        leftRight = helper(grid)
        topBottom = helper(tGrid)
        
        topBottom = [[topBottom[j][i] for j in range(m)] for i in range(n)]
        
        ans = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: 
                    l = 0
                    while i + l < n and j + l < m and grid[i + l][j] == grid[i][j + l] == 1: 
                        if leftRight[i + l][j] + l == leftRight[i + l][j + l]:
                            if topBottom[i][j + l] + l == topBottom[i + l][j + l]:
                                ans = max(ans, (l + 1)**2)
                                
                        l += 1                        
                  
        return ans
