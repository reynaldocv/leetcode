# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def helper(word):
            ans = ""
            
            for char in word: 
                ans += values[char]
                
            return int(ans)
        
        values = {chr(ord("a") + i): str(i) for i in range(10)}
        
        return helper(firstWord) + helper(secondWord) == helper(targetWord)
        
