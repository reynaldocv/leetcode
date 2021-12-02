# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:        
        aux, naux, n = [], 0, len(s)
        
        for i in range(n):
            if naux > 0 and s[i] == aux[naux - 1]:
                aux.pop()
                naux -= 1
            else:
                aux.append(s[i])
                naux += 1
            
        return "".join(aux)
                
                
        
