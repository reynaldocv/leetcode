# https://leetcode.com/problems/distance-between-bus-stops/

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        aSum = sum(distance)
        
        tmp = 0 
        
        for i in range(min(start, destination), max(start, destination)):
            tmp += distance[i]
            
        return min(tmp, aSum - tmp)
                
            
