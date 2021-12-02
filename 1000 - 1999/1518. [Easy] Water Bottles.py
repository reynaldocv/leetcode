# https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        restBottles = numBottles
        while restBottles >= numExchange: 
            quo = restBottles // numExchange
            res = restBottles % numExchange
            restBottles = quo + res
            ans += quo
        return ans
            
            
        
