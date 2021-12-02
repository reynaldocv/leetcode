# https://leetcode.com/problems/largest-plus-sign/

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        if n**2 - len(mines) == 0:
            return 0
        
        mat = [[1 for j in range(n)] for i in range(n)]
        for (x, y) in mines: 
            mat[x][y] = 0
    
        for i in range(n):
            val = 1        
            for j in range(n):
                mat[i][j] = val if mat[i][j] != 0 else 0 
                val = val + 1 if mat[i][j] != 0 else 1                 
            val = 1        
            for j in range(n - 1, -1, -1):
                mat[i][j] = min(val, mat[i][j]) if mat[i][j] != 0 else 0 
                val = val + 1 if mat[i][j] != 0 else 1 
        
        for j in range(n):         
            val = 1        
            for i in range(n):
                mat[i][j] = min(val, mat[i][j]) if mat[i][j] != 0 else 0 
                val = val + 1 if mat[i][j] != 0 else 1 
            val = 1        
            for i in range(n - 1, -1, -1):
                mat[i][j] = min(val, mat[i][j]) if mat[i][j] != 0 else 0 
                val = val + 1 if mat[i][j] != 0 else 1 

        ans = 1
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                ans = max(ans, mat[i][j])
        
        return ans
                
    
