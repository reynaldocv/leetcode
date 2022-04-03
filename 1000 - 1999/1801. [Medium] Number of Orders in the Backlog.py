# https://leetcode.com/problems/number-of-orders-in-the-backlog/

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        buy, sell = [], []
        
        for (price, amount, orderType) in orders: 
            if orderType == 0: 
                heappush(buy, [-price, amount])
            else: 
                heappush(sell, [price, amount])
                
            while buy and sell and -buy[0][0] >= sell[0][0]:
                cnt = min(buy[0][1], sell[0][1])
                buy[0][1] -= cnt
                sell[0][1] -= cnt
                
                if buy[0][1] == 0: 
                    heappop(buy)
                    
                if sell[0][1] == 0: 
                    heappop(sell)
        
        return (sum(q for _, q in sell) + sum(q for _, q in buy)) % MOD
        
