# https://leetcode.com/problems/calculate-amount-paid-in-taxes/

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0 
        
        prev = 0 
        
        for (upper, percent) in brackets: 
            if income > 0: 
                tmp = min(upper - prev, income)

                ans += percent*tmp/100

                income -= tmp
                
                prev = upper
                
            else: 
                break 
                
        return ans 
