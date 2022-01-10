# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = {day: True for day in days}
        prices = [inf for i in range(366)]
        prices[0] = 0 
        
        for day in range(1, 366):
            if day in days: 
                for (duration, cost) in [(0, costs[0]), (6, costs[1]), (29, costs[2])]:
                    last = min(365, day + duration)
                    prices[last] = min(prices[last], prices[day - 1] + cost) 
            
            else: 
                prices[day] = min(prices[day], prices[day - 1])
                
        return prices[-1]
