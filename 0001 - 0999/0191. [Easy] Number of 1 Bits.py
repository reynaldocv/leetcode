# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:        
        ans = 0
        while n > 0: 
            if n % 2 == 1: 
                ans += 1
            n = n//2
        return ans
        
