# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        if n == 0: return False
        idx = -1
        for i in range(n):
            if s[i] != "1":
                idx = i
                break
        if idx != -1:
            return False if "1" in s[idx:] else True
        else:
            return True
                
                
