# https://leetcode.com/problems/binary-gap/

class Solution:
    def binaryGap(self, n: int) -> int:
        def DecToBin(n):
            if n <= 0: return 0
            return (n % 2) + 10*DecToBin(n//2)
        
        aux = str(DecToBin(n))
        n, l, ans = len(aux), 1, 0
        print(aux)
        for i in range(1, n):
            if aux[i] == "0": 
                l += 1
            else:  
                ans = max(l, ans) 
                l = 1
                       
                
            
        return ans
