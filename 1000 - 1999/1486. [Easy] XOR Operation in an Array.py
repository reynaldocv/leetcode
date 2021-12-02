# https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        i = 1
        while i < n:
            ans = ans^(2*i + start)
            i += 1
        return ans        
