# https://leetcode.com/problems/valid-number/

class Solution:
    def isNumber(self, s: str) -> bool:
        def inGrammar(pattern, word):
            aux = re.search(pattern, word)
            return aux.span()[1] - aux.span()[0] == len(word) if aux else False
        
        s = s.replace("E", "e")
       
        pattern1 = "^[\+|\-]{0,1}(([0-9]*[\.][0-9]+)|([0-9]+[\.][0-9]*)|([0-9]+))"
        pattern2 = "^[\+|\-]{0,1}[0-9]+"
        
        if "e" not in s: 
            return inGrammar(pattern1, s)
        else: 
            words = s.split("e")
            if len(words) == 1: 
                return inGrammar(pattern2, words[0])
            elif len(words) == 2:     
                return inGrammar(pattern1, words[0]) and inGrammar(pattern2, words[1])
            else: 
                return False
        
        
        
