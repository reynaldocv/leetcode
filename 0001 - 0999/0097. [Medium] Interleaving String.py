# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        idxS1, idxS2 = 0, 0
        n, m, l = len(s1), len(s2), len(s3)
        
        if l != m + n:
            return False
        
        board = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        board[0][0] = True
        for j in range(1, m + 1):
            board[0][j] = board[0][j -1] and s2[j - 1] == s3[j - 1]
        for i in range(1, n + 1):
            board[i][0] = board[i -1][0] and s1[i - 1] == s3[i - 1]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if board[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    board[i][j] = board[i - 1][j]
                if board[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    board[i][j] = board[i][j - 1]
                
        return board[n][m]
