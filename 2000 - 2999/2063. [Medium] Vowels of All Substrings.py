# https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0
        n = len(word)
        
        for (i, char) in enumerate(word):
            if char in "aeiou":
                ans += (i + 1)*(n - i)
        
        return ans
        
     
