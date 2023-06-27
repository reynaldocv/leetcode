# https://leetcode.com/problems/battleships-in-a-board/

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def helper(x, y):
            board[x][y] = "."
            
            stack = [(x, y)]
            
            while stack: 
                (x, y) = stack.pop() 
                
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < m and 0 <= q < n: 
                        if board[p][q] == "X":                            
                            board[p][q] = "."
                            
                            stack.append((p, q))
                            
            return 1 
        
        m, n = len(board), len(board[0])
        
        ans = 0 
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    ans += helper(i, j)
                    
        return ans 
        
                    
        
        
        
