# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def helper(player):
            for i in range(3):                
                if (i, 0) in seen[player] and (i, 1) in seen[player] and (i, 2) in seen[player]: 
                    return True
                
                if (0, i) in seen[player] and (1, i) in seen[player] and (2, i) in seen[player]: 
                    return True
                
            if (0, 0) in seen[player] and (1, 1) in seen[player] and (2, 2) in seen[player]: 
                return True
            
            if (2, 0) in seen[player] and (1, 1) in seen[player] and (0, 2) in seen[player]: 
                return True
            
            return False
        
        seen = defaultdict(lambda: set())
        
        values = ["A", "B", "Draw", "Pending"]
        
        n = len(moves)
        
        for (i, (x, y)) in enumerate(moves):
            seen[i % 2].add((x, y))
            
            if helper(i % 2):
                return values[i % 2]
            
        if n == 9: 
            return values[2]
        
        else: 
            return values[3]
