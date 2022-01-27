# https://leetcode.com/problems/maximum-score-from-removing-stones/

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        aSum = a + b + c
        maxElem = max(a, b, c)
        
        if aSum - maxElem < maxElem:
            return aSum - maxElem
        else: 
            return aSum//2
        
      
        
