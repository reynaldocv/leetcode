# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {i: chr(i + ord("a")) for i in range(26)}
        dicS, dicP = {}, {}
        arrS = s.split(" ")
        aux, aux2 = "", ""
        
        idx = 0
        for elem in arrS: 
            if elem not in dicS: 
                dicS[elem] = dic[idx]
                idx += 1
        for elem in arrS: 
            aux += dicS[elem]
        
        idx = 0        
        for elem in pattern: 
            if elem not in dicP: 
                dicP[elem] = dic[idx]
                idx += 1
        for elem in pattern: 
            aux2 += dicP[elem]
        
        
        return aux == aux2
                
