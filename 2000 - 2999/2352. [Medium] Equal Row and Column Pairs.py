# https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        counter = defaultdict(lambda: 0)
        
        for i in range(n):
            counter[tuple(grid[i])] += 1 
            
        grid = [[grid[j][i] for j in range(n)] for i in range(n)]
        
        ans = 0 
        
        for i in range(n):
            key = tuple(grid[i])
            ans += counter[key]
            
        return ans 
        
            
