# https://leetcode.com/problems/least-operators-to-express-number/

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @cache
        def helper(val): 
            if val < x: 
                return min(2*val - 1, 2*(x - val))
            
            k = int(log(val)//log(x))
            ans = k + helper(val - x**k)
            
            if x**(k + 1) < 2*val: 
                ans = min(ans, k + 1 + helper(x**(k + 1) - val))
            
            return ans 
        
        return helper(target)
        
