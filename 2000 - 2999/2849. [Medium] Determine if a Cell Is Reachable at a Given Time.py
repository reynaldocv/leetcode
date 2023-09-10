# https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        witdh = abs(sx - fx)
        heigh = abs(sy - fy)
        
        distance = witdh + heigh - min(witdh, heigh) 
        
        if distance == t: 
            return True 
        
        if distance == 0: 
            distance = 2
        
        if distance > t: 
            return False 
        
        return True 
