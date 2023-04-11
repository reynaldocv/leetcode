# https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        remain = 0 
        
        ans = 0 
        
        while numBottles: 
            ans += numBottles
            
            total = numBottles + remain 
            
            numBottles = total//numExchange
            
            remain = total % numExchange
            
        return ans 
            
            
            
            
        
