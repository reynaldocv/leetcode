# https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def helper(arr):
            tmp = ""
            
            for char in arr + ["#"]:
                if char != "#":
                    tmp += char
                    
                else: 
                    if len(tmp) == l: 
                        if collaborator(tmp, word):
                            return True 
                        
                        if collaborator(tmp[:: -1], word):
                            return True 
                    
                    tmp = ""
            
            return False 
        
        def collaborator(tmp, word):
            for (i, char) in enumerate(tmp):
                if char != " ":
                    if char != word[i]:
                        return False 
            
            return True 
        
        m, n, l = len(board), len(board[0]), len(word)
        
        for row in board: 
            if helper(row):
                return True 
            
        board = [[board[i][j] for i in range(m)] for j in range(n)]
        
        for row in board: 
            if helper(row):
                return True 
            
        return False 
        
        
        
