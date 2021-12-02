# https://leetcode.com/problems/distance-between-bus-stops/

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        totaldistance = sum(distance)
        if start > destination: 
            start, destination = destination, start
        aux = 0
        for i in range(start, destination):
            aux += distance[i]
        
        return min(totaldistance - aux, aux)
        
