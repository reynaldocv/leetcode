# https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def compare(s1, s2):
            for i in range(w):
                if s1[i] != " ":
                    if s1[i] == s2[i]:
                        continue
                    else: 
                        return False                
            return True
        
        n, m = len(board), len(board[0])
        w = len(word)
        spaces = []      
        
        for i in range(n):
            prev = ""
            for j in range(m):
                if board[i][j] == "#":
                    if len(prev) == w:
                        spaces.append(prev)
                    prev = ""
                else: 
                    prev += board[i][j]
            if len(prev) == w:
                spaces.append(prev)
            
        for j in range(m):
            prev = ""
            for i in range(n):
                if board[i][j] == "#":
                    if len(prev) == w:
                        spaces.append(prev)
                    prev = ""
                else: 
                    prev += board[i][j]
            if len(prev) == w:
                spaces.append(prev)

        for space in spaces: 
            if space == " "*w:
                return True
            elif compare(space, word) or compare(space[::-1], word):
                return True
        
        return False
                
        
        
