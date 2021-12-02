# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        def isLower(l):
            return True if abs(ord(l) - ord("a")<= 26) else False
        def isUpper(l):
            return True if abs(ord(l) - ord("A")<= 26) else False        
        
        FILO = []
        n = len(s)
        for i in range(n):
            letter = s[i]
            if len(FILO) > 0: 
                if isLower(FILO[len(FILO) - 1]) and isUpper(letter):
                    if FILO[len(FILO) - 1] == letter.lower():
                        FILO.pop()
                    else:
                        FILO.append(letter)
                elif isUpper(FILO[len(FILO) - 1]) and isLower(letter): 
                    if FILO[len(FILO) - 1] == letter.upper():
                        FILO.pop()
                    else:
                        FILO.append(letter)
                else:
                    FILO.append(letter)
            else:
                FILO.append(letter)
        
        return "".join(FILO)
