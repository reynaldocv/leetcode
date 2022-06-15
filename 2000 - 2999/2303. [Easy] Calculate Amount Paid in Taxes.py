# https://leetcode.com/problems/calculate-amount-paid-in-taxes/

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        prev = 0 
        ans = 0 
        
        for (upper, percent) in brackets: 
            if income > 0:
                val = min(upper - prev, income)
                ans += val*percent/100                
                income -= val 
            else: 
                break 
                
            prev = upper
                
        return ans 
