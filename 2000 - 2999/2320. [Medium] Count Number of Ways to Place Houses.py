# https://leetcode.com/problems/count-number-of-ways-to-place-houses/

class Solution:
    def countHousePlacements(self, n: int) -> int:
        @cache
        def helper(m):
            if m < 1: 
                return 1
            else: 
                return helper(m - 1) + helper(m - 2)
        
        MOD = 10**9 + 7
        
        return pow(helper(n), 2, MOD)
