# https://leetcode.com/problems/count-square-sum-triples/

class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n):            
            for b in range(a + 1, n):
                c = int((a**2 + b**2)**.5)
                if c <= n:
                    if c**2 == a**2 + b**2:
                        ans += 2
                else: 
                    break 
        return ans
                
