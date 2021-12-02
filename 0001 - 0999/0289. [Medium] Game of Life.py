# https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def helper(val, x, y, matrix):
            ans = 0 
            for (i, j) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                r, s = x + i, y + j
                if 0 <= r < n and 0 <= s < m: 
                    if matrix[r][s] == val: 
                        ans += 1
            
            return ans
    
        n, m = len(board), len(board[0])
        matrix = [[board[i][j] for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1: 
                    quantity = helper(1, i, j, matrix)
                    if quantity < 2 or quantity > 3: 
                        board[i][j] = 0 
                else: 
                    quantity = helper(1, i, j, matrix)
                    if quantity == 3: 
                        board[i][j] = 1
                        
                        
                
            
