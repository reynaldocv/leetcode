# https://leetcode.com/problems/battleships-in-a-board/

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def helper(x, y, val):
            for (i, j) in [(1, 0), (0, 1)]:
                r, s = x + i, y + j
                if 0 <= r < n and 0 <= s < m: 
                    if board[r][s] == "X":
                        board[r][s] = val
                        helper(r, s, val)
                        
        n, m = len(board), len(board[0])
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == "X":
                    ans += 1
                    board[i][j] = ans
                    helper(i, j, ans)
                    
        return ans
                    
        
        
        
