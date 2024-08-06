# https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        @cache 
        def helper(x0, x1, y0, y1):
            if x1 - x0 == 1 and y1 - y0 == 1: 
                return 0 
            
            else: 
                ans = inf 
                
                if x1 - x0 > 1:                 
                    for x in range(x0 + 1, x1):
                        ans = min(ans, verticalCut[x - 1] + helper(x0, x, y0, y1) + helper(x, x1, y0, y1))
                        
                if y1 - y0 > 1: 
                    for y in range(y0 + 1, y1):
                        ans = min(ans, horizontalCut[y - 1] + helper(x0, x1, y0, y) + helper(x0, x1, y, y1))

                return ans 
            
        return helper(0, n, 0, m)
                    
                
