# https://leetcode.com/problems/sum-of-digits-in-base-k/

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n > 0:
            ans += (n%k)
            n = n//k
        return ans
        
