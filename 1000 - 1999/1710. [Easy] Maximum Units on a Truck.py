# https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda item: -item[1])
        
        ans = 0 
        for (boxes, units) in boxTypes: 
            if boxes <= truckSize: 
                truckSize -= boxes 
                ans += boxes*units
                
            else: 
                ans += truckSize*units 
                break 
                
        return ans 
            
