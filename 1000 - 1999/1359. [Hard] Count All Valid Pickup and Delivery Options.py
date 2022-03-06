# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 1
        
        for i in range(1, n + 1):
            ans *= i
            ans *= 2*i - 1
            
            ans %= MOD
            
        return ans 
    
class Solution2:
    def countOrders(self, n: int) -> int:
        @cache
        def helper(unpicked, undelivered):
            if not unpicked and not undelivered: 
                return 1 
            
            if (unpicked < 0 or undelivered < 0 or undelivered < unpicked):
                return 0 
            
            ans = unpicked*helper(unpicked - 1, undelivered)
            ans %= MOD
            
            ans += (undelivered - unpicked)*helper(unpicked, undelivered - 1)
            ans %= MOD
            
            return ans 
        
        MOD = 10**9 + 7
        return helper(n, n)
