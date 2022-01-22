# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans = 0 
        cost.sort(reverse = True)
        
        n = len(cost)
        
        for i in range(0, n, 3):
            ans += cost[i]
            ans += cost[i + 1] if i + 1 < n else 0 
            
        return ans
        
