# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = ""
        for i in range(26):
            letters += chr(ord("a") + i)
            letters += chr(ord("A") + i)
        
        aux = ""
        for letter in s: 
            if letter in letters: 
                aux += letter
        aux = aux[::-1]
        
        ans = ""
        
        j = 0
        for letter in s: 
            if letter in letters: 
                ans += aux[j]
                j += 1            
            else: 
                ans += letter
        
        return ans
