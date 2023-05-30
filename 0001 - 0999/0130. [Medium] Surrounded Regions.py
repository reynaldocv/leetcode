class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def helper(x, y, newValue):
            stack = [(x, y)]            
            seen.add((x, y))
            
            board[x][y] = newValue
            
            while stack: 
                (x, y) = stack.pop()
                
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < m and 0 <= q < n and board[p][q] == "O" and (p, q) not in seen: 
                        seen.add((p, q))
                        
                        board[p][q] = newValue
                        stack.append((p, q))
            
        m, n = len(board), len(board[0])
        
        stack = set() 
        
        for i in range(m):
            stack.add((i, 0))
            stack.add((i, n - 1))
            
        for j in range(n):
            stack.add((0, j))
            stack.add((m - 1, j))
            
        seen = set()
        
        for (i, j) in stack: 
            if board[i][j] == "O" and (i, j) not in seen:                
                helper(i, j, "O")
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in seen: 
                    board[i][j] = "X"
                    
        
