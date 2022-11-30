# https://leetcode.com/problems/find-the-pivot-integer/

class Solution:
    def pivotInteger(self, n: int) -> int:
        tmp = n*(n + 1)//2
        prev = 0 
        
        for i in range(1, n + 1):
            prev += i 
            
            if 2*prev == tmp + i: 
                return i 
            
        return -1
