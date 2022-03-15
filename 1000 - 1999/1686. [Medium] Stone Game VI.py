# https://leetcode.com/problems/stone-game-vi/

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)        
        heap = []
        
        for i in range(n):
            x, y = aliceValues[i], bobValues[i]
            heappush(heap, (- x - y, x, y))
            
        alice = bob = 0 
        turn = True
        
        while heap: 
            _, x, y = heappop(heap)
            if turn: 
                alice += x
            else: 
                bob += y
                
            turn = not turn 
            
        if alice == bob: 
            return 0 
        
        return 1 if alice > bob else -1
