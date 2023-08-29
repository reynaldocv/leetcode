# https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        left = 0 
        right = sum(1 for customer in customers if customer == "Y")
        
        ans = (right, 0)
        
        for (i, customer) in enumerate(customers): 
            if customer == "Y":
                right -= 1 
                
            else: 
                left += 1 
                
            ans = min(ans, (right + left, i + 1))
            
        return ans[1]
        
        
        
        
