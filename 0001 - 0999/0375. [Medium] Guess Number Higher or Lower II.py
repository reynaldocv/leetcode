# https://leetcode.com/problems/guess-number-higher-or-lower-ii/

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def helper(start, end):
            if start >= end: 
                return 0 
            else: 
                money = inf
                for i in range(start, end + 1):
                    money = min(money, i + max(helper(start, i - 1), helper(i + 1, end)))
                    
                return money
            
        return helper(1, n)
