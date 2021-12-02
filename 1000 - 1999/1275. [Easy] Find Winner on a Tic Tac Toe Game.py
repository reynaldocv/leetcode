# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def rowValue(a):
            x = a[0]
            for i in range(1, 3):
                if a[i] != x:
                    return ""
            return "" if x == " " else x
            
        michi = [[" " for i in range(3)] for j in range(3)]
        m = "A"
        for (i, j) in moves:
            michi[i][j] = m
            m = "A" if m == "B" else "B"
        
        michi2 = [[michi[i][j] for i in range(3)] for j in range(3)]
       
        ans = ""
        for i in range(3):
            ans += rowValue(michi[i])
            ans += rowValue(michi2[i])
            
        ans += rowValue([michi[0][0], michi[1][1], michi[2][2]])
        ans += rowValue([michi[2][0], michi[1][1], michi[0][2]])
        
        if len(ans) >= 1:
            return ans[0] 
        elif len(moves) == 9:
            return "Draw"
        else: 
            return "Pending"
