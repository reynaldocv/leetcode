# https://leetcode.com/problems/closest-dessert-cost/

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        toppings=[]
        def helper(i, total):
            if i == m:
                toppings.append(total)
            else: 
                helper(i + 1, total + 2*toppingCosts[i])
                helper(i + 1, total + toppingCosts[i])
                helper(i + 1, total)
                
        m = len(toppingCosts)
        
        helper(0, 0)
        
        ans = (inf, inf)
        for base in baseCosts: 
            for topping in toppings: 
                ans = min(ans, (abs(target - (base + topping)), base + topping))
                
        return ans[1]
        
            
        
        
        
