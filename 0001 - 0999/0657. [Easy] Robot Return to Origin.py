# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = {"R":0, "L":0, "U":0, "D":0}
        for i in moves:
            counter[i] = counter.get(i, 0) + 1
        return (counter["D"] == counter["U"] and counter["R"] == counter["L"])
            
        
