# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def square(i, j, board):
            ans = []
            for k in range(3*i, 3*i + 3):
                for l in range(3*j, 3*j + 3):
                    ans.append(board[k][l])
            return ans
        
        
        def repeated(arr):
            dic = {}
            for i in arr: 
                if i != "." and i in dic: 
                    return False
                else: 
                    dic[i] = True
            return True
        
        ans = True
        for row in board: 
            ans = ans and repeated(row)
        
        if ans: 
            board2 = [[board[i][j] for i in range(9)] for j in range(9)]
            for row in board2: 
                ans = ans and repeated(row)
            if ans: 
                for i in range(3):
                    for j in range(3):
                        arr = square(i, j, board)
                        ans = ans and repeated(arr)
                return ans
            else: 
                return False        
        else: 
            return False
