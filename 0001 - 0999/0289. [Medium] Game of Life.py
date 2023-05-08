# https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        tmp = [[board[i][j] for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                count = 0 
                
                for (r, s) in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
                    x, y = i + r, j + s
                    
                    if 0 <= x < m and 0 <= y < n: 
                        if tmp[x][y] == 1: 
                            count += 1 
                
                if tmp[i][j] == 0 and count == 3: 
                    board[i][j] = 1 
                    
                if tmp[i][j] == 1 and not (2 <= count <= 3): 
                    board[i][j] = 0 
                    
    
        
        
                        
                
            
