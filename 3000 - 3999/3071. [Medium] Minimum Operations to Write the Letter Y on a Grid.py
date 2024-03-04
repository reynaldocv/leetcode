# https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid) 
        
        counterY = defaultdict(lambda: 0)
        counterZ = defaultdict(lambda: 0)
        
        for i in range(n):
            for j in range(n):
                counterZ[grid[i][j]] += 1 
                
        x, y = n//2, n//2 
        
        counterY[grid[x][y]] += 1 
        counterZ[grid[x][y]] -= 1
        
        for i in range(1, n//2 + 1):
            p, q = x - i, y - i    
            
            counterY[grid[p][q]] += 1 
            counterZ[grid[p][q]] -= 1
            
            p, q = x - i, y + i    
            
            counterY[grid[p][q]] += 1 
            counterZ[grid[p][q]] -= 1
            
            p, q = x + i, y
            
            counterY[grid[p][q]] += 1 
            counterZ[grid[p][q]] -= 1
            
        totalY = n + n//2
        totalZ = n**2 - totalY 
        
        ans = inf 
                
        for i in range(3):
            for j in range(3):
                if i != j: 
                    ans = min(ans, totalY - counterY[i] + totalZ - counterZ[j])
                    
        return ans 
            
