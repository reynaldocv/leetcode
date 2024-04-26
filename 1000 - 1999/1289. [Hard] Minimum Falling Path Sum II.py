# https://leetcode.com/problems/minimum-falling-path-sum-ii/

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid) 
        
        minVal = [(0, i) for i in range(2)]
        
        for i in range(n):
            newMinVal = []
            
            for j in range(n):
                if j == minVal[0][1]:
                    grid[i][j] += minVal[1][0]
                    
                else: 
                    grid[i][j] += minVal[0][0]
                    
                insort(newMinVal, (grid[i][j], j))
                
                newMinVal = newMinVal[: 2]
                
            minVal = newMinVal
                        
        return min(grid[-1])
        
                
