# https://leetcode.com/problems/brick-wall/

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall) 
        
        counter = defaultdict(lambda: 0)        
        maxCounter = 0 
        
        for row in wall: 
            prev = 0 
            
            for num in row[: -1]:
                prev += num                 
                counter[prev] += 1 
                
                maxCounter = max(maxCounter, counter[prev])
        
        return n - maxCounter
        
                
        
        
        
