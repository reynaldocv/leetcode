# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        dp = [0 for _ in range(total + 1)]
        
        for cost in [cost1, cost2]:
            for i in range(cost, total + 1):
                dp[i] += dp[i - cost] + 1
                
        return max(dp) + 1
        
class Solution2:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0 
        
        for i in range(total//cost1 + 1):
            aux = total - cost1*i
            
            ans += aux//cost2 + 1
            
        return ans 
            
