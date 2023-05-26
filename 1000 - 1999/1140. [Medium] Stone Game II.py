# https://leetcode.com/problems/stone-game-ii/

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def helper(start, M):
            if n - start <= 2*M: 
                return piles[start]
                
            else: 
                ans = 0 
                for x in range(1, 2*M + 1):
                    ans = max(ans, piles[start] - helper(start + x, max(M, x)))
                
                return ans
        
        n = len(piles)
        
        for i in range(n - 1):
            piles[n - i - 2] += piles[n - i - 1]
            
        return helper(0, 1)
