# https://leetcode.com/problems/account-balance-after-rounded-purchase/

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        unit = purchaseAmount % 10
        
        if unit <= 4: 
            purchaseAmount -= unit
        
        else: 
            purchaseAmount += 10 - unit
            
        return 100 - purchaseAmount
