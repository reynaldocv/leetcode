# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        aux = ["" for i in range(numRows)]
        
        n = len(s)
        
        j = 0
        ratio = 1
        
        for i in range(n):
            aux[j] += s[i]            
            if j == numRows - 1: 
                ratio = -1
                
            elif j == 0:                
                ratio = 1
                
            j += ratio

        return "".join(aux)
