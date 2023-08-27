# https://leetcode.com/problems/furthest-point-from-origin/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counter = defaultdict(lambda: 0)
        
        for move in moves: 
            counter[move] += 1
            
        return abs(counter["R"] - counter["L"]) + counter["_"]
        
