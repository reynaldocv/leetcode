# https://leetcode.com/problems/find-the-winning-player-in-coin-game/

class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        time = 0 
        
        while x >= 1 and y >= 4: 
            x -= 1 
            y -= 4 
            
            time = (time + 1) % 2 
            
        return "Alice" if time == 1 else "Bob"
            
        
        
        
