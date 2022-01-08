# https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
      
class Solution2:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def helper(start, end, turn):
            if start == end: 
                return turn*piles[start]
            else: 
                val1 = piles[start] + helper(start + 1, end, -turn)
                val2 = piles[end] + helper(start, end - 1, -turn)
                
                return max(val1, val2)
        
        n = len(piles)
        
        return helper(0, n - 1, 1) > 0
            
            
        
