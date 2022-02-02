# https://leetcode.com/problems/minimum-falling-path-sum-ii/

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def helper(arr, idx):
            ans = (inf, inf)
            for (i, num) in enumerate(arr):
                if i != idx: 
                    ans = min(ans, (num, i))
            
            return ans
        
        n = len(grid)
        
        if n == 1: 
            return grid[0][0]
        
        for i in range(n - 2, -1, -1):
            (minElem1, idx1) = helper(grid[i + 1], -1)
            (minElem2, idx2) = helper(grid[i + 1], idx1)
            for j in range(n):
                if j != idx1: 
                    grid[i][j] += minElem1
                else: 
                    grid[i][j] += minElem2
                    
        return min(grid[0])
        
                
