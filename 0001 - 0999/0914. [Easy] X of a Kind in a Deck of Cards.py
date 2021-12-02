# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def MCD (a, b):
            if a % b == 0: 
                return b
            else: 
                return MCD(b, a % b)
        
        dic = {}
        for card in deck: 
            dic[card] = dic.get(card, 0) + 1
            
        card = deck[0]
        ans = dic[card]
        for k in dic: 
            ans = MCD(ans, dic[k]) 
                            
        return False if ans == 1 else True
                
        
        
        
