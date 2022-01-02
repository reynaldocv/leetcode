# https://leetcode.com/problems/check-if-move-is-legal/

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        if board[rMove][cMove] != ".":
            return False
        
        newColor = "B" if color == "W" else "W"
        
        for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            cnt = 0 
            x = rMove + r
            y = cMove + s
            while 0 <= x < 8 and 0 <= y < 8 and board[x][y] == newColor:
                x, y = x + r, y + s
                cnt += 1
                
            if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == color:
                if cnt >= 1: 
                    return True
                
        return False
                    
