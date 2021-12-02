# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        aux, aux2= "", ""
        for i in range(n):
            if s[i] == " ":
                if aux != "":
                    aux2 = aux 
                aux = ""
            else:
                aux += s[i]
        if aux != "":
            aux2 = aux
        
        return len(aux2)
