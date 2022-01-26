# https://leetcode.com/problems/clumsy-factorial/

class Solution:
    def clumsy(self, n: int) -> int:
        def helper(m, k, sign):
            if k == 4: 
                return int(m*(m - 1)//(m - 2)) + sign*(m - 3)
            elif k == 3: 
                return int(m*(m - 1)//(m - 2))
            elif k == 2: 
                return m*(m - 1)
            elif k == 1:
                return m
            
        ans = helper(n, min(n, 4), 1)
        
        n -= 4
        while n > 0: 
            ans -= helper(n, min(n, 4), -1)
            n -= 4 
            
        return ans
            
        
