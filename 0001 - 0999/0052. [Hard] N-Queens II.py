# https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        def helper(row):
            nonlocal ans  
            
            if row == n:
                ans += 1 
                
            else: 
                for col in range(0, n):
                    d1 = (row + col)
                    d2 = (row - col)
                    
                    if col not in visitedCols:                        
                        if d2 not in secondDiagonal: 
                            if d1 not in firstDiagonal: 
                                visitedCols.add(col)
                                firstDiagonal.add(d1)
                                secondDiagonal.add(d2)

                                helper(row + 1)

                                firstDiagonal.remove(d1)
                                secondDiagonal.remove(d2)                                
                                visitedCols.remove(col)

        ans = 0 
        
        visitedCols = set() 
        firstDiagonal = set() 
        secondDiagonal = set() 
        
        helper(0)
        
        return ans 
                        
