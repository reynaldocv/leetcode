# https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1: 
            return 1
        
        modulo = 10**9 + 7
        return (2**p - 1)*pow(2**p - 2, (2**(p - 1) - 1), modulo) % modulo
        
        
