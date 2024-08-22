# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = [0]
        
        prev = prices[0]
        
        for price in prices[1: ]:
            left.append(max(left[-1], price - prev))
            
            prev = min(prev, price)
        
        right = [0]
        
        prev = prices[-1]
        
        for price in prices[: -1][:: -1]:
            right.insert(0, max(prev - price, right[0]))
        
            prev = max(prev, price)
            
        n = len(prices)
        
        ans = 0 
       
        for i in range(n):
            l = 0 if i - 1 < 0 else left[i]
            r = right[i]
            
            ans = max(ans, l + r)
            
        return ans 
        
        
        
        
