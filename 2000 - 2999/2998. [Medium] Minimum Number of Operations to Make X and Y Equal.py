# https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @cache
        def helper(x, y):
            if y >= x: 
                return y - x
            
            else: 
                ans = x - y
                
                ans = min(ans, 1 + helper(x - 1, y))
                
                for val in [5, 11]:                
                    if x % val == 0: 
                        ans = min(ans, 1 + helper(x//val, y))
                    
                    else: 
                        res = val - (x % val)
                        
                        ans = min(ans, 1 + res + helper(x//val + 1, y))
                        
                return ans 
            
        return helper(x, y)
