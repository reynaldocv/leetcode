# https://leetcode.com/problems/elimination-game/

class Solution:
    def lastRemaining(self, n: int) -> int:
        m = n
        ratio = 1
        start = 1
        count = 1
        while start + ratio <= n:            
            if count == 1: 
                start += ratio
            else: 
                start = start + ratio if (m % 2 == 1) else start            
            count = (count + 1) % 2
            ratio *= 2
            m = m//2
            
        return start
            
        
