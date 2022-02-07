# https://leetcode.com/problems/mirror-reflection/

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        common = gcd(p, q)
        p //= common
        q //= common
        
        if q % 2 == 0:
            return 0
        elif p % 2 == 0:
            return 2 
        else: 
            return 1

        
