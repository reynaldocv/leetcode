# https://leetcode.com/problems/design-neighbor-sum-service/

class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.n = n = len(grid)
        
        self.matrix = grid
        
        self.index = {}
        
        for i in range(n):
            for j in range(n):
                self.index[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        (x, y) = self.index[value]
        
        ans = 0
        
        for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:        
            p, q = x + r, y + s             
            
            if 0 <= p < self.n and 0 <= q < self.n: 
                ans += self.matrix[p][q]
                
        return ans

    def diagonalSum(self, value: int) -> int:
        (x, y) = self.index[value]
        
        ans = 0
            
        for (r, s) in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            p, q = x + r, y + s 
            
            if 0 <= p < self.n and 0 <= q < self.n: 
                ans += self.matrix[p][q]
                
        return ans

# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
