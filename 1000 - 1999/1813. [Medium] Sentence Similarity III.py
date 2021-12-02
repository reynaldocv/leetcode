# https://leetcode.com/problems/sentence-similarity-iii/

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2: 
            return True
        
        if len(sentence2) < len(sentence1):
            sentence1, sentence2 = sentence2, sentence1
            
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        
        n, m = len(s1), len(s2)
        
        for i in range(n + 1):
            prefix = " ".join(s1[:i])             
            sufix = " ".join(s1[i:])
            
            p, s = len(prefix), len(sufix)
            
            prefix2 = " ".join(s2[:i])
            sufix2 = " ".join(s2[m - n + i:])
            
            if prefix == prefix2 and sufix == sufix2:
                return True
            
        return False
