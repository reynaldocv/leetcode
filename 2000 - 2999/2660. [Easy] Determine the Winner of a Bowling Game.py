# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        
        first = 0
        second = 0 
        
        counter1 = 0 
        counter2 = 0 
        
        for i in range(n):
            if first > 0: 
                counter1 += 2*player1[i]
            
            else: 
                counter1 += player1[i]
            
            if second > 0: 
                counter2 += 2*player2[i]
            
            else: 
                counter2 += player2[i]
                
            first -= 1 
            second -= 1 
                
            if player1[i] == 10: 
                first = 2
                
            if player2[i] == 10: 
                second = 2
                
        if counter1 > counter2: 
            return 1
        
        elif counter2 > counter1: 
            return 2 
        
        return 0 
            
                
                
            
        
