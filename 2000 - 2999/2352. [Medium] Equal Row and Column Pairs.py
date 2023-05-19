# https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        trasversal = [[grid[i][j] for i in range(n)] for j in range(n)]
        
        counter = defaultdict(lambda: 0)
        
        for row in grid:
            counter[tuple(row)] += 1 
            
        ans = 0 
        
        for row in trasversal: 
            ans += counter[tuple(row)]
                
        return ans 
                
        
            
