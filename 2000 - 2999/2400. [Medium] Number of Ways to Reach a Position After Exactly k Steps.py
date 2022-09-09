# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        @cache
        def helper(steps, x):
            if steps == 0:
                if x == startPos: 
                    return 1 
                else: 
                    return 0 
            else: 
                return helper(steps - 1, x - 1) + helper(steps - 1, x + 1)
            
        MOD = 10**9 + 7
        
        return helper(k, endPos) % MOD
