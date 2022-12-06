# https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0 
        
        boxTypes.sort(key = lambda item: item[1])
        
        while truckSize and boxTypes:
            (quantity, units) = boxTypes.pop()
            
            if quantity <= truckSize: 
                truckSize -= quantity
                ans += quantity*units
                
            else: 
                ans += truckSize*units                
                truckSize = 0
                
        return ans 
                
