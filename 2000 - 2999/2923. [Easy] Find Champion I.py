# https://leetcode.com/problems/find-champion-i/

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        defeat = defaultdict(lambda: set())
        
        for i in range(n):
            for j in range(n):
                if i != j and grid[i][j] == 1: 
                    defeat[i].add(j)
                    
                    if len(defeat[i]) == n - 1:
                        return i 
        
        return -1
                    
                      
