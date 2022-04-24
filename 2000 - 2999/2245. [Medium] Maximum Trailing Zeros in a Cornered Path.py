# https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        f2 = [[0]*n for _ in range(m)]
        f5 = [[0]*n for _ in range(m)]
        
        for i in range(m): 
            for j in range(n): 
                x = grid[i][j]
                while x % 2 == 0: 
                    f2[i][j] += 1
                    x //= 2 
        
                x = grid[i][j]
                while x % 5 == 0: 
                    f5[i][j] += 1
                    x //= 5 
        
        h = [[[0, 0] for j in range(n + 1)] for i in range(m + 1)]
        v = [[[0, 0] for j in range(n + 1)] for i in range(m + 1)]

        for i in range(m): 
            for j in range(n): 
                h[i][j + 1][0] = h[i][j][0] + f2[i][j]
                h[i][j + 1][1] = h[i][j][1] + f5[i][j]
                v[i + 1][j][0] = v[i][j][0] + f2[i][j]
                v[i + 1][j][1] = v[i][j][1] + f5[i][j]
        
        ans = 0 
        for i in range(m): 
            for j in range(n): 
                hh = [h[i][n][0] - h[i][j][0], h[i][n][1] - h[i][j][1]]
                vv = [v[m][j][0] - v[i][j][0], v[m][j][1] - v[i][j][1]]
                
                ans = max(ans, min(h[i][j][0] + v[i][j][0] + f2[i][j], h[i][j][1] + v[i][j][1] + f5[i][j]))
                ans = max(ans, min(h[i][j][0] + vv[0], h[i][j][1] + vv[1]))
                ans = max(ans, min(hh[0] + v[i][j][0], hh[1] + v[i][j][1]))
                ans = max(ans, min(hh[0] + vv[0] - f2[i][j], hh[1] + vv[1] - f5[i][j]))
                
        return ans
