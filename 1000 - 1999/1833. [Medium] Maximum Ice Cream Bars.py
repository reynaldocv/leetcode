# https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort() 
        
        ans = 0 
        
        for cost in costs: 
            if coins < cost: 
                return ans 
            
            else: 
                ans += 1 
                
                coins -= cost
                
        return ans 
        
