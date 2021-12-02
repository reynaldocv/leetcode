# https://leetcode.com/problems/shortest-completing-word/

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dic = {}
        for i in licensePlate:
            i = i.lower()
            if 0 <= (ord(i) - ord("a")) <= 26:
                dic[i] = dic.get(i, 0) + 1
        
        print(dic)
        ans = ""
        nans = inf
        for word in words:
            aux = {}        
            for i in word: 
                if i in dic: 
                    aux[i] = aux.get(i, 0) + 1                  
            
            go = True            
            for i in dic: 
                if i not in aux or dic[i] > aux[i]:
                    go = False
                    break
                
            if go:                
                if nans > len(word):
                    nans = len(word)
                    ans = word
        return ans
                
