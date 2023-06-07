# https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def helper(time):
            ans = 0 
            
            for rank in ranks: 
                ans += int((time/rank)**.5)
                
            return ans >= cars
        
        start = 0 
        end = min(ranks)*cars**2
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if helper(middle):
                end = middle 
            else: 
                start = middle 
                
        return end 
            
