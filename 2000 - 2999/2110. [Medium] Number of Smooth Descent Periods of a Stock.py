# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        prev = inf
        ans = 0 
        cnt = 0 
        for price in prices: 
            if prev - 1 == price:
                cnt += 1                 
            else: 
                cnt = 1
            
            prev = price
            ans += cnt
            
        return ans
                
                
        
