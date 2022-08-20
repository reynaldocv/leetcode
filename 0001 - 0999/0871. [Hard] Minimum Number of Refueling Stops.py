# https://leetcode.com/problems/minimum-number-of-refueling-stops/

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        tank = startFuel
        
        stations.append([target,float("inf")])
        
        ans = 0
        prev = 0
        
        for i in range(len(stations)):
            tank -= stations[i][0] - prev 
        
            while heap and tank < 0:
                tank += -heappop(heap)
                ans += 1
                
            if tank < 0:
                return -1
            
            heappush(heap, -stations[i][1])
            prev = stations[i][0]
        
        return ans
