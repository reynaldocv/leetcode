# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        m = int(math.log(n, 2)) + 1
        l = len(s)
        seen = {0: True}
        
        for i in range(l):
            prev = 0
            for j in range(i, min(i + m + 1, l)):
                prev = 2*prev + int(s[j])
                if prev <= n:
                    seen[prev] = True
                
        return n + 1 == len(seen)
