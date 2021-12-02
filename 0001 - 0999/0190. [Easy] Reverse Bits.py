# https://leetcode.com/problems/reverse-bits/

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0: return 0
        ans, power =0, 31
        while n: 
            ans += (n & 1) << power
            n = n >> 1
            power -= 1            
        return ans
            
