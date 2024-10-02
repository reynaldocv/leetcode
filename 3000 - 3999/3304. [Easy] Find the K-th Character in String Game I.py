# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution:
    def kthCharacter(self, k: int) -> str:
        def helper(word):
            ans = word 
            
            for char in word:
                ans += letter[(index[char] + 1) % 26]
                
            return ans
        
        index = {chr(ord("a") + i): i for i in range(26)}
        letter = {i: chr(ord("a") + i) for i in range(26)}
        
        word = "a"
        
        while len(word) < k:            
            word = helper(word)
            
        return word[k - 1]
