# https://leetcode.com/problems/stone-game-ix/

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        counter = defaultdict(lambda: 0)
        for stone in stones: 
            counter[stone % 3] += 1
                
        if counter[0] % 2 == 1: 
            return abs(counter[1] - counter[2]) > 2            
        else: 
            return 1 in counter and 2 in counter  
            
        
        
