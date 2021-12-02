# https://leetcode.com/problems/ugly-number-iii/

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def mcd(a, b):
            if b == 0: 
                return a
            else: 
                return mcd(b, a % b)
        
        def mcm(a, b):
            return a*b//mcd(a, b)
        
        def numberofmultiples(n, a, b, c):
            return n//a + n//b + n//c - n//mcm(a,b) - n//mcm(b, c) - n//mcm(a, c) + n//mcm(mcm(a,b), c)       
        
        start = 0
        end = n*min(a, b, c)
        
        while end - start > 1: 
            m = (end + start)//2
            if numberofmultiples(m, a, b, c) < n: 
                start = m 
            else: 
                end = m 
    
        return end
        
        
