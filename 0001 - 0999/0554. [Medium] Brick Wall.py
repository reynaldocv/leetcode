# https://leetcode.com/problems/brick-wall/

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        aux = 0        
        counter = {}
        for row in wall: 
            dist = 0 
            for i in range(len(row) - 1):
                dist += row[i]
                counter[dist] = counter.get(dist, 0) + 1
                aux = max(aux, counter[dist])
        
        return n - aux
                
                
        
        
        
