# https://leetcode.com/problems/stickers-to-spell-word/

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def helper(t):
            k = tuple(t.items())
            
            if k not in memo:
                ans = inf                 
                if not t: 
                    ans = 0
                else:                 
                    for s in stk: 
                        if t & s: 
                            ans = min(ans, 1 + helper(t - s))

                memo[k] = ans
            
            return memo[k]

        if set(target) - reduce(lambda a, b: a|b, map(set,stickers)): 
            return -1

        stk, memo = list(map(Counter,stickers)), {}
        
        return helper(Counter(target))
