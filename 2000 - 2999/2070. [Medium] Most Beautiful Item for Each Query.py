# https://leetcode.com/problems/most-beautiful-item-for-each-query/

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        
        prices = [price for (price, _) in items]
        beauties = [beauty for (_, beauty) in items]
        n = len(items)
        
        for i in range(1, n):
            beauties[i] = max(beauties[i], beauties[i - 1])
            
        ans = []
        for querie in queries: 
            idx = bisect_right(prices, querie)
            if idx == 0: 
                ans.append(0)
            else:
                ans.append(beauties[idx - 1])                
            
        return ans
            
        
        
