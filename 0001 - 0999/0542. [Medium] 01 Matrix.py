# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:        
        points = []
        n = len(mat)
        m = len(mat[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    points.append((i, j))
                    visited[i][j] = True
                    
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(points):
            (x, y) = points.pop(0)
            val = mat[x][y]
            for (i, j) in directions: 
                r = x + i
                s = y + j
                if 0 <= r < n and 0 <= s < m: 
                    if visited[r][s] == False:
                        visited[r][s] = True            
                        mat[r][s] = val + 1                                            
                        points.append((r, s))

        return mat
      
class Solution2:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:        
        points = []
        n = len(mat)
        m = len(mat[0])
       
        ans = [[inf for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0: 
                    ans[i][j] = 0 
                else:
                    if i > 0: 
                        ans[i][j] = min(ans[i][j], ans[i - 1][j] + 1)                        
                    if j > 0: 
                        ans[i][j] = min(ans[i][j], ans[i][j - 1] + 1)
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i < n - 1: 
                    ans[i][j] = min(ans[i][j], ans[i + 1][j] + 1)                        
                if j < m - 1: 
                    ans[i][j] = min(ans[i][j], ans[i][j + 1] + 1)
                    
        return ans

                    
