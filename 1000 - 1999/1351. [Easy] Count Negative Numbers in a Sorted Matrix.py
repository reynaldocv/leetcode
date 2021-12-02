# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        ans = 0
        for r in range(row): 
            for c in range(col):
                if grid[r][c] < 0:
                    ans += col - c
                    break
        return ans
        
