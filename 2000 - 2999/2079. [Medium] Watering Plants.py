# https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        can = capacity
         
        for (i, water) in enumerate(plants):
            if can >= water:
                ans += 1
                can -= water
            else:                 
                can = capacity - water
                ans += 2*(i) + 1
                
        return ans
        
        
