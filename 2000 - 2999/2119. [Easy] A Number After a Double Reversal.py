# https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def helper(num):
            return int(str(num)[::-1])
        
        return num == helper(helper(num))
