# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

class Solution:
    def numOfWays(self, n: int) -> int:            
        MOD = 10**9 + 7        
        num = [6,6]
        
        for i in range(1,n):
            n1 = num[0]
            n2 = num[1]
            num[0] = n1*2 + n2*2
            num[1] = n1*2 + n2*3
        
        return sum(num) % MOD
        
        
