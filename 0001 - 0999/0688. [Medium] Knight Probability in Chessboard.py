# https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[row][column] = 1 
        
        for _ in range(k):
            dp2 = [[0 for _ in range(n)] for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for (x, y) in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                        p, q = r + x, c + y
                        if 0 <= p < n and 0 <= q < n: 
                            dp2[p][q] += dp[r][c]/8.0
                            
            dp = dp2
            
        ans = sum(sum(row) for row in dp)
        
        return ans
        
