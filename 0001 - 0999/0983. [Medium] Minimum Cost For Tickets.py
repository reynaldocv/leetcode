# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:      
        limit = days[-1]
        
        dp = [0] + [inf for _ in range(limit)]
        
        days = {day for day in days}
        
        for i in range(limit + 1):
            if i in days: 
                for (ith, j) in enumerate([1, 7, 30]):
                    last = min(limit, i + j - 1)
                    
                    dp[last] = min(dp[last], dp[i - 1] + costs[ith])
                    
            else: 
                dp[i] = min(dp[i], dp[i - 1])
                
        return dp[-1]
        
class Solution2:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache 
        def helper(x):
            if x == n: 
                return 0 
            
            ans = inf 
            
            for (i, r) in enumerate([1, 7, 30]):
                y = days[x] + r 
                
                idx = bisect_left(days, y)
                
                ans = min(ans, costs[i] + helper(idx))
                
            return ans 
        
        n = len(days)
        
        return helper(0)
        
