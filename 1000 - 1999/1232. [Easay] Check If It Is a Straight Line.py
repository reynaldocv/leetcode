# https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def helper(x, y, p, q):
            if x == p: 
                return "inf"
            
            else: 
                return (y - q)/(x - p)
            
        counter = set()
        
        n = len(coordinates)
        
        for i in range(1, n):
            (x, y) = coordinates[0]
            (p, q) = coordinates[i]
            
            counter.add(helper(x, y, p, q))
                        
            if len(counter) > 1: 
                return False 
            
        return True 
                     
