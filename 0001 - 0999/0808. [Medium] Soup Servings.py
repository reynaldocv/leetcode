# https://leetcode.com/problems/soup-servings/

class Solution:
    def soupServings(self, n: int) -> float:                
        @cache
        def helper(a, b):
            if a <= 0 and b <= 0: 
                return 0.5
            
            if a <= 0: 
                return 1
            
            if b <= 0: 
                return 0
            
            ans = helper(a - 100, b)
            ans += helper(a - 75, b - 25)
            ans += helper(a - 50, b - 50)
            ans += helper(a - 25, b - 75)
            
            return ans/4
            
        if n > 5000: 
            return 1 
                
        return helper(n, n)
