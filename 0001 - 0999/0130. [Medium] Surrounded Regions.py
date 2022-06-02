class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        seen = set()
        
        for j in range(n):
            if board[0][j] == "O":
                seen.add((0, j))
            if board[m - 1][j] == "O":
                seen.add((m - 1, j))
                
        for i in range(m):
            if board[i][0] == "O":
                seen.add((i, 0))
            if board[i][n - 1] == "O":
                seen.add((i, n - 1))
                
        stack = [(x, y) for (x, y) in seen]
                    
        while stack: 
            (x, y) = stack.pop()
            for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                p, q = x + r, y + s 
                if 0 <= p < m and 0 <= q < n: 
                    if (p, q) not in seen and board[p][q] == "O": 
                        stack.append((p, q))
                        seen.add((p, q))
                        
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen: 
                    board[i][j] = "X"
