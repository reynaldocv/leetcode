# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(i, j, char):
            x, y = i//3, j//3            
            for r in range(9):
                if r == i: 
                    continue
                if board[r][j] == char: 
                    return False
            
            for s in range(9):
                if s == j:
                    continue
                if board[i][s] == char: 
                    return False
                
            for r in range(3*x, 3*x + 3):
                for s in range(3*y, 3*y + 3):
                    if r == i and s == j: 
                        continue
                    if board[r][s] == char: 
                        return False
            
            return True
        
        def helper(i, j):
            if i == 9: 
                return True
            elif j == 9: 
                return helper(i + 1,  0)
            elif board[i][j] == ".":
                for char in "123456789":
                    if not isValid(i, j, char):
                        continue
                    
                    board[i][j] = char
                    if helper(i, j + 1):
                        return True
                    
                    board[i][j] = "."
                return False
            else: 
                return helper(i, j + 1)           
            
        return helper(0, 0)
        
    
    
	
    
    
                
                
            
            
            
        
