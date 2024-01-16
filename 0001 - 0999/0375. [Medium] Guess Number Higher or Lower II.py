# https://leetcode.com/problems/guess-number-higher-or-lower-ii/

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def helper(start, end):
            if start >= end: 
                return 0 
            
            else: 
                ans = inf
                
                for num in range(start, end + 1):
                    ans = min(ans, num + max(helper(start, num - 1), helper(num + 1, end)))
                    
                return ans
            
        return helper(1, n)
