# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arrS = s.split(" ")
        aux = []
        
        for i in range(len(arrS)):
            try: 
                val = int(arrS[i])
                aux.append(val)
            except: 
                continue
        
        for i in range(len(aux) - 1):
            if aux[i] < aux[i + 1]:
                continue
            else: 
                return False
    
        return True
            
        
        
        
