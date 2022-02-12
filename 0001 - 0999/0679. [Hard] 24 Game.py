# https://leetcode.com/problems/24-game/

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def helper(cards): 
            if len(cards) == 1: 
                return round(cards[0], 4) == 24
            else: 
                arr = [(i, card) for (i, card) in enumerate(cards)]
                
                for ((i, card1), (j, card2)) in combinations(arr, 2):
                    newCards = {card1 + card2, card1*card2, abs(card1 - card2)}
                    if card2 != 0:
                        newCards.add(card1/card2)
                    if card1 != 0:
                        newCards.add(card2/card1)
                        
                    oldCards = [card for (k, card) in enumerate(cards) if k != i  and k != j]
                    
                    if any (helper(oldCards + [card]) for card in newCards):
                        return True
                    
                return False
                
        return helper(cards)
