# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = [s]
        existed = {s: True}
        while len(words) > 0: 
            word = words.pop()
            if word == "":
                return True
            for w in wordDict: 
                if w in word and word.index(w) == 0: 
                    aux = word.replace(w, "", 1)
                    if aux not in existed:
                        words.append(aux)
                        existed[aux] = aux
                        
        return False
