# https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        l = len(grid)
        for i in range(l):
            ans += max(grid[i])
        for i in range(l):
            aux = [grid[j][i] for j in range(l)]
            ans += max(aux)
        for i in range(l):
            for j in range(l):
                if grid[i][j] != 0:
                    ans += 1
        return ans
                
                
