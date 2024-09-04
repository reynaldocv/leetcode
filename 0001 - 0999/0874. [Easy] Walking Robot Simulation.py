# https://leetcode.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        k = 0
        
        seen = {(x, y) for (x, y) in obstacles}
        
        ans = 0 
        
        (x, y) = (0, 0)
        
        for value in commands: 
            if value == -1:
                k = (k + 1) % 4
                
            elif value == -2:
                k = (k - 1) % 4 
                
            else: 
                for _ in range(value):
                    x, y = x + direction[k][0], y + direction[k][1]
                    
                    if (x, y) in seen: 
                        x, y = x - direction[k][0], y - direction[k][1]
                        
                        break 
                        
                ans = max(ans, x**2 + y**2)
                
        return ans
                    
