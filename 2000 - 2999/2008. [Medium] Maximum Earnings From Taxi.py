# https://leetcode.com/problems/maximum-earnings-from-taxi/

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0 for _ in range(n + 1)]
        rideIter, i = 0, 1
        r = len(rides)
        rides.sort(key = lambda item: item[1])
        
        while i <= n:
            if rideIter < r and rides[rideIter][1] == i: 
                (start, end, tip) = rides[rideIter]
                cost = end - start + tip
                dp[i] = max(dp[i], dp[start] + cost)
                rideIter += 1
                continue
            dp[i] = max(dp[i], dp[i - 1])
            i += 1
            
        return dp[-1]
        
