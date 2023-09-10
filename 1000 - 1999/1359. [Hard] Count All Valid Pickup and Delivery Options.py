# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        
        ans = 1 
        
        for num in range(2, 2*n + 1):
            if num % 2 == 0: 
                num //= 2 
            
            ans = (ans * num) % MOD
            
        return ans
