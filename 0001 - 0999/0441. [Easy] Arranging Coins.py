# https://leetcode.com/problems/arranging-coins/ 

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1: 
            return 1
        
        m = int((2*n)**.5)        
        
        while m*(m + 1)//2 <= n:
            m += 1
            
        return m - 1
        
class Solution2:
    def arrangeCoins(self, n: int) -> int:
        def helper(val):
            return val*(val + 1)//2 <= n
        
        start = 0 
        end = n + 1
        
        while end - start > 1:
            mid = (end + start)//2
            if helper(mid):
                start = mid
            else: 
                end = mid
                
        return start 
