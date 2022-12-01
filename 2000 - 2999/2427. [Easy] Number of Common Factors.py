# https://leetcode.com/problems/number-of-common-factors/

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        common = gcd(a, b)
        
        ans = 0 
        
        for i in range(1, common + 1):
            if common % i == 0: 
                ans += 1 
                
        return ans 
        
