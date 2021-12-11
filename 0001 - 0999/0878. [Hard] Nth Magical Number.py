# https://leetcode.com/problems/nth-magical-number/

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def helper(m, a, b): 
            common = gcd(a,b)
            if common  != 1:
                return helper(m//common, a//common, b//common)
            else:
                ans = m//a
                ans += m//b
                ans -= m//(a*b)
            
                return ans
            
        MOD = 10**9 + 7
        start = 1
        end = max(a, b)*n
        
        while end - start > 1: 
            m = (end + start)//2
            if helper(m,a,b) >= n: 
                end = m
            else: 
                start = m
                
        return end % MOD
