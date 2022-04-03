# https://leetcode.com/problems/number-of-orders-in-the-backlog/

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy, sell = [], []
        
        for (p, q, t) in orders: 
            if t: 
                heappush(sell, [p, q])
            else: 
                heappush(buy, [-p, q])
            
            while buy and sell and -buy[0][0] >= sell[0][0]: 
                qty = min(buy[0][1], sell[0][1])
                buy[0][1] -= qty
                sell[0][1] -= qty
                
                if buy[0][1] == 0: 
                    heappop(buy)
                if sell[0][1] == 0: 
                    heappop(sell)
                    
        MOD = 10**9 + 7
        
        return (sum(q for _, q in sell) + sum(q for _, q in buy)) % MOD
    
