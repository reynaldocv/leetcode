# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution:
    def minSwaps(self, s: str) -> int:
        filo = []
        for char in s: 
            if len(filo) > 0 and (filo[len(filo) - 1] == "[" and char == "]"):
                filo.pop()
            else: 
                filo.append(char)
        n = len(filo)
        
        return n//4 if n % 4 == 0 else n//4 + 1
