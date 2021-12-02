# https://leetcode.com/problems/path-crossing/

class Solution:
    def isPathCrossing(self, path: str) -> bool: 
        values = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
        dic = {(0, 0): True}
        
        x, y = 0, 0
        dic[(x, y)] = True
        for i in path:
            (i, j) = values[i]
            if (x + i, y + j) in dic: 
                return True
            dic[(x + i, y + j)] = True
            x, y = x + i, y + j
        return False
            
