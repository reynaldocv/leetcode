# https://leetcode.com/problems/orderly-queue/

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1: 
            n = len(s)
            minS = s
            for i in range(1, n):
                newS = s[i:] + s[:i]
                minS = min(minS, newS)
            return minS
        else: 
            return "".join(sorted(s))
        
        
