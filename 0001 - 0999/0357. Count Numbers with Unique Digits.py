# https://leetcode.com/problems/count-numbers-with-unique-digits/

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        if n == 0: 
            return 1
        
        aux = [0]*8
        aux[0] = 10
        aux[1] = 81
        ans = aux[0] if n == 1 else aux[0] + aux[1]
        for i in range(2, n):
            aux[i] = aux[i - 1]*(10 - i)
            ans += aux[i]
            
        return ans
        
        
            
