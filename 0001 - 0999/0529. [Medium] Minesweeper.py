# https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board and not(board[0]): 
            return board
        
        m, n = len(board), len(board[0])
        
        stack = [tuple(click)]
        
        dirs = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
        
        while stack: 
            (x, y) = stack.pop(0)
            if board[x][y] == "M":
                board[x][y] = "X"
                continue
            
            cnt = 0 
            neighbors = []
            for (r, s) in dirs: 
                p, q = x + r, y + s
                if 0 <= p < m and 0 <= q < n: 
                    if board[p][q] == "M":
                        cnt += 1
                    elif board[p][q] == "E":
                        neighbors.append((p, q))
                        
            if cnt > 0: 
                board[x][y] = str(cnt)
            else: 
                board[x][y] = "B"
                for (p, q) in neighbors: 
                    board[p][q] = "B"
                    stack.append((p, q))
        
        return board
                    
                
        

        
