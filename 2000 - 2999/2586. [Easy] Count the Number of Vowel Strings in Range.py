# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        
        for word in words[left: right + 1]:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                ans += 1 
                
        return ans 
                
                
        
