# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        aux = s[:k]
        seen = {aux: 1}
        for char in s[k:]:
            aux = aux[1:] + char
            seen[aux] = 1
            
        return len(seen) == 2**k
        
      
            

        
        
