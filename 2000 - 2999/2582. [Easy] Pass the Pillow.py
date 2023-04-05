# https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        odd = n - 1
        eve = 2*(n - 1)
        
        remain = time % eve
        
        if remain <= odd: 
            return 1 + remain
        
        else: 
            return n - (remain % odd)
            
        
