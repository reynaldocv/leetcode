# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = inf
        seen = {}
        
        for (i, card) in enumerate(cards):
            if card in seen:
                ans = min(ans, i - seen[card] + 1)
            
            seen[card] = i 
            
        return -1 if ans == inf else ans 
        
