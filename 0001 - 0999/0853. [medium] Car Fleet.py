# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        
        arr = [(position[i], speed[i]) for i in range(n)]
        
        arr.sort()
        
        last = 0 
        
        ans = 0 
        
        for (position, speed) in arr[:: -1]:
            endTime = (target - position)/speed
            
            if endTime > last: 
                ans += 1 
              
                last = endTime
            
        return ans 
