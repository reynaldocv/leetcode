# https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        
        ans = [0 for _ in range(n)]
        
        put = True 
        idx = 0 
        
        i = 0 
        
        deck.sort() 
        
        while i < n:
            if ans[idx] == 0:
                if put: 
                    ans[idx] = deck[i]
                    i += 1 
                    
                    put = False 
                
                else:
                    put = True 
                    
            idx = (idx + 1) % n
            
        return ans 
            
                
