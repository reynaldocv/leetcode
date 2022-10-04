# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def helper():
            for i in range(9):
                seen = set()
                for val in board[i]:
                    if val != ".":
                        if val not in seen: 
                            seen.add(val)
                        else: 
                            return False 
            
            return True 
        
        def collaborator(row, col):
            seen = set()
            for i in range(3*row, 3*(row + 1)):
                for j in range(3*col, 3*(col + 1)):
                    val = board[i][j]
                    
                    if val != ".":
                        if val not in seen: 
                            seen.add(val)
                        else: 
                            return False 
                        
            return True 
    
        if not helper():
            return False 
        
        board = [[board[j][i] for j in range(9)] for i in range(9)]
        
        if not helper():
            return False 
        
        for i in range(3):
            for j in range(3):        
                if not collaborator(i, j):
                    return False 
                
        return True
        
        
        
        
        
        
        
        
        
        
        
