# https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for (i, cost) in enumerate(costs):
            coins -= cost     
            if coins <= 0: 
                return i + 1 if coins == 0 else i
            
        return len(costs)
    
