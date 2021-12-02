# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        def DecToBin(n):
            if n < 2: return n
            return (n % 2) + 10*DecToBin(n//2)
        
        n = str(DecToBin(n))
        ans = True
        for i in range(len(n) - 1):
            if n[i] == n[i + 1]:
                ans = False
                break
        return ans
        
