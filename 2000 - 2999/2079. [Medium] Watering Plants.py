# https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        
        can = capacity
        
        for (i, plant) in enumerate(plants):
            if plant > can:
                ans += 2*i + 1
                
                can = capacity - plant 
                
            else: 
                ans += 1 
                
                can -= plant
                
        return ans 
                
        
