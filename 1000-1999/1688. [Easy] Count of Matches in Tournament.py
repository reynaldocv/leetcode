# https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        def matches(n):
            if n <= 1: return 0
            if n % 2 == 0:
                return n//2 + matches(n//2)
            else:
                return 1 + n//2 + matches(n//2)
        
        return matches(n)
        
