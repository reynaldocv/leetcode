# https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        for i in range(n - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        
        ans  = ""
        for i in range(n):
            ans += chr((((ord(s[i]) - ord("a")) + shifts[i]) % 26) + ord("a"))
        
        return ans
        
        
        
