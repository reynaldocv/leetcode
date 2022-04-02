# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0 
        while goal or start: 
            bit1 = goal & 1 
            bit2 = start & 1
            if bit1 != bit2: 
                ans += 1
            
            goal //= 2 
            start //= 2 
            
        return ans 
