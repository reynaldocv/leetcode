# https://leetcode.com/problems/available-captures-for-rook/

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        x, y = -1, -1
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    x, y = i, j
        ans = 0               
        for i in range(1, 8):
            if x + i < 8:
                if board[x + i][y] == "p":
                    ans += 1
                    break
                if board[x + i][y] == "B":
                    break
            else:
                break
        
        for i in range(1, 8):
            if x - i >= 0:
                if board[x - i][y] == "p":
                    ans += 1
                    break
                if board[x - i][y] == "B":
                    break
            else:
                break
        
        for i in range(1, 8):
            if y + i < 8:
                if board[x][y + i] == "p":
                    ans += 1
                    break
                if board[x][y + i] == "B":
                    break
            else:
                break
                
        for i in range(1, 8):
            if y - i >= 0:
                if board[x][y - i] == "p":
                    ans += 1
                    break
                if board[x][y - i] == "B":
                    break
            else:
                break
        
    
        
        return ans
