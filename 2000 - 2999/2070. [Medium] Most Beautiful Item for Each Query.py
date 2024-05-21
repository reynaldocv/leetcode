# https://leetcode.com/problems/most-beautiful-item-for-each-query/

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        
        prices = [0]
        dp = [0]
        
        maxBeauty = 0
        
        for (price, beauty) in items:
            maxBeauty = max(maxBeauty, beauty)
            
            prices.append(price)
            dp.append(maxBeauty)
        
        ans = []
            
        for query in queries:
            idx = bisect_right(prices, query) - 1
            
            ans.append(dp[idx])
        
        return ans
            
        
        
