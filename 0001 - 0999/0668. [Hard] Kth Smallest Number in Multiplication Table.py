# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def helper(x):
            count = 0 
            for i in range(1, m + 1):
                count += min(x//i, n)
            
            return count >= k
        
        start, end = 1, n*m
        
        while end - start > 0: 
            mid = (end + start)//2
            if not helper(mid):
                start = mid + 1
            else: 
                end = mid
                
        return start
            
        
