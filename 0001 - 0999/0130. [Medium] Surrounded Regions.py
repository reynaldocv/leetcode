# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def helper(x, y):
            allPoints = {(x, y): True}
            points = [(x, y)]
            limited = True 
            while points:
                (x, y) = points.pop()
                if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                    limited = False
                for (i, j) in directions: 
                    r, s = x + i, y + j
                    if 0 <= r < n and 0 <= s < m:
                         if board[r][s] == "O" and (r, s) not in allPoints:
                            points.append((r, s))
                            allPoints[(r, s)] = True
                           
            if limited: 
                for (x, y) in allPoints: 
                    board[x][y] = "X"
            else:
                for (x, y) in allPoints: 
                    board[x][y] = "Y"
        
        n = len(board)
        m = len(board[0])
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if board[i][j] == "O":
                    helper(i, j)
                    
        for i in range(n):
            for j in range(m):
                board[i][j] = "O" if board[i][j] == "Y" else board[i][j]                    
        
