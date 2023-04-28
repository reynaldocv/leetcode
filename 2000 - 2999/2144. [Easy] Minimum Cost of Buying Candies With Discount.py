# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans = 0 
        
        cost.sort(key = lambda item: -item)
        
        for (i, num) in enumerate(cost):
            if (i % 3) < 2: 
                ans += num 
                
        return ans 
        
