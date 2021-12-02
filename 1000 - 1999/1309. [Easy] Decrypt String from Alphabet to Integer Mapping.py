# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        codes = {}
        for i in range(10, 27):
            codes[str(i) + "#"] = chr(97 + i - 1)
        
        for i in codes:
            s = s.replace(i, codes[i])
            
        for i in range(1,10): 
            s = s.replace(str(i), chr(96 + i))
            
        return s
        
