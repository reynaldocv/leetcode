# https://leetcode.com/problems/valid-tic-tac-toe-state/

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        seen = defaultdict(lambda: 0)
        lines = defaultdict(lambda: 0)
        for sentence in board: 
            lines[sentence] += 1
            for char in sentence: 
                seen[char] += 1
                
        if seen["X"] - seen["O"] < 0 or seen["X"] - seen["O"] > 1 : 
            return False 
        
        for j in range(3):
            aux = ""
            for i in range(3):
                aux += board[i][j]
                
            lines[aux] += 1
        
        lines[board[0][0] + board[1][1] + board[2][2]] += 1
        lines[board[0][2] + board[1][1] + board[2][0]] += 1
        
        if lines["XXX"] > 0 and lines["OOO"] > 0: 
            return False
        elif lines["XXX"] > 0:
            if seen["X"] <= seen["O"]:
                return False
        elif lines["OOO"] > 0:
            if seen["X"] > seen["O"]:
                return False
        
        return True
        
        
