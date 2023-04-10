# https://leetcode.com/problems/available-captures-for-rook/

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def helper(x, y, r, s):
            while 0 <= x < 8 and 0 <= y < 8: 
                if board[x][y] == "p":
                    return 1
                
                elif board[x][y] == "B":
                    return 0 
                
                x, y = x + r, y + s
                
            return 0
        
        (x, y) = (0, 0)
        
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    (x, y) = (i, j)
                    
                    break 
               
        ans = 0 
        
        for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ans += helper(x, y, r, s)
            
        return ans 
                    
