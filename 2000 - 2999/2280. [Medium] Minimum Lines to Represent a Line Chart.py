# https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        
        if n == 1: 
            return 0 
        
        stockPrices.sort()
        
        (x1, y1) = stockPrices[1]
        (x0, y0) = stockPrices[0]
        
        common = gcd(y1 - y0, x1 - x0)
        
        angle = ((y1 - y0)//common, (x1 - x0)//common) 
        ans = 1 
        
        for i in range(2, n):
            (x1, y1) = stockPrices[i]
            (x0, y0) = stockPrices[i - 1]
        
            common = gcd(y1 - y0, x1 - x0)
        
            newAngle = ((y1 - y0)//common, (x1 - x0)//common) 
        
            if newAngle != angle: 
                ans += 1 
                angle = newAngle
            
        return ans    
