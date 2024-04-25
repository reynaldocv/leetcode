# https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter:

    def __init__(self, words: List[str]):
        self.value = {}
        
        for (ith, word) in enumerate(words): 
            prefix = ""
            
            for char in word: 
                prefix += char 
                
                suffix = ""
                
                for char in word[:: -1]:
                    suffix = char + suffix
                    
                    self.value[(prefix, suffix)] = ith
                
    def f(self, pref: str, suff: str) -> int:
        if (pref, suff) not in self.value:
            return -1 
        
        return self.value[(pref, suff)]
        
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
