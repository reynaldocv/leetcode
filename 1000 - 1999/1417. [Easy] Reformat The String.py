# https://leetcode.com/problems/reformat-the-string/

class Solution:
    def reformat(self, s: str) -> str:
        def isLetter(n):
            return True if (0 <= ord(n) - ord("a") <= 26) else False
        
        aux1, aux2 = "", ""
        for i in s: 
            if isLetter(i):
                aux1 += i
            else:
                aux2 += i
        
        ans = ""
        if abs(len(aux1) - len(aux2)) <= 1:            
            if len(aux1) == len(aux2):
                for i in range(len(aux1)):
                    ans += aux1[i] + aux2[i] 
            else: 
                if len(aux1) < len(aux2):
                    aux1, aux2 = aux2, aux1
                for i in range(len(aux2)):  
                    ans += aux1[i] + aux2[i]
                ans += aux1[len(aux1) - 1]
        return ans
        
