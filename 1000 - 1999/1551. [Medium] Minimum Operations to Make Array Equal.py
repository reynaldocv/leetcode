# https://leetcode.com/problems/minimum-operations-to-make-array-equal/

class Solution:
    def minOperations(self, n: int) -> int:        
        m = n // 2 
        
        if n % 2 == 0: 
            return m**2 
        
        else: 
            return m*(m + 1)
        
