# https://leetcode.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dic = {(x, y): True for (x, y) in obstacles}        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, ans = 0, 0, 0
        idx = 0
        for i in range(len(commands)):            
            command = commands[i]
            if command == -1:
                idx = (idx + 1) % 4
            if command == -2:
                idx = (idx - 1 + 4) % 4
            if 1 <= command <= 9:
                for j in range(command):
                    if (x + directions[idx][0], y + directions[idx][1]) not in dic:
                        x = x + directions[idx][0]
                        y = y + directions[idx][1]
                    else:
                        break
            
            ans = max(ans, x**2 + y**2)                                   
        return ans
