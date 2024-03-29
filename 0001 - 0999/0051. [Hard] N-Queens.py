# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def helper(i):
            if i == n: 
                ans.append(["".join(row) for row in board])
                
            else: 
                for j in range(n):
                    if j not in vertical and i + j not in diagonal1 and i - j not in diagonal2: 
                        vertical.add(j)
                        diagonal1.add(i + j)
                        diagonal2.add(i - j)
                        
                        board[i][j] = "Q"
                        
                        helper(i + 1)
                        
                        board[i][j] = "."
                        
                        vertical.remove(j)
                        diagonal1.remove(i + j)
                        diagonal2.remove(i - j)
            
        board = [["." for _ in range(n)] for _ in range(n)]
        
        ans = []
        
        vertical = set()
        diagonal1 = set() 
        diagonal2 = set()
        
        helper(0)
        
        return ans 


        
