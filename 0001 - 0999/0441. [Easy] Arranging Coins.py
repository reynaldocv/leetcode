# https://leetcode.com/problems/arranging-coins/ 

class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 0 
        end = n + 1
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if mid*(mid + 1) <= 2*n:
                start = mid 
            else: 
                end = mid 
                
        return start 
        
