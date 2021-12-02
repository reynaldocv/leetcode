# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]        
        n = len(matrix)
        m = len(matrix[0])        
        visited = [[False for j in range(m)] for i in range(n)]
        x, y = 0, 0 
        ans = []
        k = 0
        while len(ans) < n*m:             
            if (x < n and y < m) and visited[x][y] == False:
                ans.append(matrix[x][y])
                visited[x][y] = True
            else: 
                x -= direction[k][0]
                y -= direction[k][1]
                k = (k + 1) % 4
            x += direction[k][0]
            y += direction[k][1]
        return ans
                    
                                       
        
