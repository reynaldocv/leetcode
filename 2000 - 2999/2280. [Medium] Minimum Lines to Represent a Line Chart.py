# https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        
        stockPrices.sort() 
        
        (dX, dY) = (0, 0)
        
        ans = 0 
        
        for i in range(1, n):
            (x0, y0) = stockPrices[i - 1]
            (x1, y1) = stockPrices[i]
            
            common = gcd(abs(x1 - x0), abs(y1 - y0))
            
            tmpX = (x1 - x0)//common
            tmpY = (y1 - y0)//common
            
            if dX == tmpX and dY == tmpY: 
                continue 
                
            else: 
                ans += 1 
                
                dX = tmpX
                dY = tmpY 
                
        return ans 
