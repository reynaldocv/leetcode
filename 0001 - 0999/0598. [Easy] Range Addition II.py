# https://leetcode.com/problems/range-addition-ii/

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        row = m
        col = n 
        
        for (r, c) in ops: 
            row = min(row, r)
            col = min(col, c)
            
        return row * col
