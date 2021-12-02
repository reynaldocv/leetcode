# https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:        
        n = len(deck)        
        arr = [" " for _ in range(n)]
        idx = 0
        flip = True
        i = 0
        while idx < n:
            if arr[i] == " ":
                if flip == True: 
                    arr[i] = idx
                    idx += 1                
                flip = not flip
            
            i = (i + 1) % n
            
        deck.sort()
        for i in range(n): 
            arr[i] = deck[arr[i]]
            
        return arr
                
