# https://leetcode.com/problems/arranging-coins/ 

class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 1
        end = n + 1
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if middle*(middle + 1)//2 <= n: 
                start = middle 
                
            else: 
                end = middle 
                
        return start
        
        
