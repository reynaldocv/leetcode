# https://leetcode.com/problems/minimum-operations-to-make-array-equal/

class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0: 
            return (n//2)**2
        else: 
            return (n//2 + 1)*(n//2)
        
