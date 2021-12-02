# https://leetcode.com/problems/range-addition-ii/

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        a, b = m, n
        for (a1, b1) in ops:
            a = min(a, a1)
            b = min(b, b1)
        return a*b
        
