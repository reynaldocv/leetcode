# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic = {}
        for word in words: 
            for w in word: 
                dic[w] = dic.get(w, 0) + 1
        
        n = len(words)
        
        for k in dic: 
            if dic[k] % n != 0: 
                return False
        
        return True
        
