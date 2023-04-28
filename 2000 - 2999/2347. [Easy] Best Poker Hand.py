# https://leetcode.com/problems/best-poker-hand/

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        suits = {suit for suit in suits}
        
        maxElem = 0
        counter = defaultdict(lambda: 0)
        
        for rank in ranks: 
            counter[rank] += 1 
            
            maxElem = max(maxElem, counter[rank])
        
        if len(set(suits)) == 1:
            return "Flush"
        
        if maxElem > 2:
            return "Three of a Kind"
        
        if maxElem > 1:
            return "Pair"
        
        return "High Card"

