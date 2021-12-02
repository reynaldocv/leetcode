# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        def lenMaxSequences(s, bit):
            l, ans = 0, 0
            n = len(s)
            for i in range(n):
                if s[i] == bit:
                    l += 1
                else:
                    ans = max(ans, l)
                    l = 0
            ans = max(ans, l)
            return ans 
        
        print(lenMaxSequences(s, "1"))
        print(lenMaxSequences(s, "0"))
        return lenMaxSequences(s, "1") > lenMaxSequences(s, "0")
            
