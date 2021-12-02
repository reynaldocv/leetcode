# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        arr = [inf for _ in range(n + 1)]
        arr[0] = 0
        
        for i in range(1, n + 1):
            aux = inf
            for j in range(1, int(i**.5) + 1):
                aux = min(aux, arr[i - j**2])
            arr[i] = aux + 1
         
        return arr[-1]
                
                
