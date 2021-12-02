# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution:
    def minTimeToType(self, word: str) -> int:
        prev = "a"
        n = len(word)
        ans = 0
        for i in range(n):
            aux1 = (ord(word[i]) - ord(prev) + 26) % 26
            aux2 = (ord(prev) - ord(word[i]) + 26) % 26
            aux = min(aux1, aux2)
            prev = word[i]
            ans += aux + 1
        
        return ans
            
        
