# https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        m = n//2
        
        costs.sort(key = lambda item: item[0] - item[1])
        
        ans = sum(a for (a, b) in costs[:m])        
        ans += sum(b for (a, b) in costs[m:])
        
        return ans
        
