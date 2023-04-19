# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        
        ans = [0 for _ in range(n)]
        
        stack = []
        
        for (i, price) in enumerate(prices + [0]):
            while stack and stack[-1][0] >= price: 
                (_, idx) = stack.pop() 
                
                ans[idx] = prices[idx] - price
                
            stack.append((price, i))
            
        return ans 
