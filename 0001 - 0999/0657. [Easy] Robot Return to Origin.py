# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = defaultdict(lambda: 0)
        
        for move in moves:
            counter[move] += 1
            
        return counter["D"] == counter["U"] and counter["R"] == counter["L"]
            
