# https://leetcode.com/problems/minimum-jumps-to-reach-home/

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        def recursive(pos, backward):
            if pos > bound or pos < 0 or pos in forbidden:
                return inf
            elif pos == x:
                return 0
            elif (pos, backward) not in memo:
                memo[pos, backward] = 1 + recursive(pos + a, False)
                if not backward:
                    memo[pos, backward] = min(memo[pos, backward], 1 + recursive(pos - b, True))
            return memo[pos, backward]
        
        forbidden = {num: True for num in forbidden}
        bound = max(max(forbidden) + a + b, x + b)
        memo = {}
        
        ans = recursive(0, True)
        return ans if ans != inf else -1
