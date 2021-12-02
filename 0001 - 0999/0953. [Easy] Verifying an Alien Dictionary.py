# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {order[i]: chr(i + ord("a")) for i in range(len(order))}
        for i in range(len(words)): 
            aux = ""
            for w in words[i]: 
                aux += dic[w]
            words[i] = aux
        
        words1 = words.copy()
        words1.sort()
        for i in range(len(words)):
            if words[i] != words1[i]:
                return False
        return True
        
