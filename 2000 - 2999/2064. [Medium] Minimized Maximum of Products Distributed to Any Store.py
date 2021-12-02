# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        start, end = 1, sum(quantities)
        while end - start > 0: 
            m = (end + start)//2
            if sum(ceil(qty/m) for qty in quantities) <= n: 
                end = m
            else: 
                start = m + 1
                
        return start
            
        
