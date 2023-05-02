# https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        
        ans = 0
        
        for i in range(k + 1):
            ans += min(tickets[i], tickets[k])
            
        for i in range(k + 1, n):
            ans += min(tickets[i], tickets[k] - 1)
            
        return ans 
            
            
