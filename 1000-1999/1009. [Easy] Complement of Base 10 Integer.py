# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0: return 1        
        complement = 0
        power = 0
        while N > 0:
            complement += (((N%2) + 1)% 2)*2**power
            N = N // 2
            power += 1
        return complement
                          
                    
        
