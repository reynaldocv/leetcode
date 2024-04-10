# https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        
        deck.sort() 
        
        arr = [i for i in range(n)]
        
        index = []
        
        while arr: 
            idx = arr.pop(0)
            
            index.append(idx)
            
            if arr: 
                arr.append(arr.pop(0))
                
        ans = [0 for i in range(n)]        
        
        for i in range(n):
            ans[index[i]] = deck[i]
            
        return ans 
        
        
                
