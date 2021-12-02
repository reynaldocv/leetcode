# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtracking(board, i, j, n, m, word, k, finalWord):
            if word == finalWord: 
                return True
            if 0 <= i < n and 0 <= j < m and finalWord[k] == board[i][j]: 
                val = board[i][j]
                board[i][j] = "*"                
                for (x, y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
                    r, s = x + i, y + j
                    if backtracking(board, r, s, n, m, word + val, k + 1, finalWord):
                        return True
                board[i][j] = val
            return False
            
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                if backtracking(board, i, j, n, m, "", 0, word):
                    return True
        return False
        
