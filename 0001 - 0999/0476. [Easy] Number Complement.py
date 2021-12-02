# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        pos = 0
        ans = 0
        while num > 0:
            ans += (((num % 2) + 1) % 2)*2**pos
            num = num//2
            pos += 1            
            
        return ans
            
