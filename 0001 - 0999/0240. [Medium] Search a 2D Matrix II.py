# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        x, y = 0, 0
        points = [[0, 0]]
        visited = [[False for j in range(m)] for i in range(n)]
        while len(points) > 0: 
            (x, y) = points.pop()
            visited[x][y] = True
            if matrix[x][y] == target: 
                return True
            else: 
                for (i, j) in directions: 
                    r, s = x + i, y + j
                    if 0 <= r < n and 0 <= s < m: 
                        if visited[r][s] == False and visited[r][s] <= target: 
                            points.append((r,s))
        return False
                    
            
