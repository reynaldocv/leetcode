# https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        counterA = [0 for _ in range(26)]
        counterB = [0 for _ in range(26)]
        
        m, n = len(a), len(b)
        
        for char in a: 
            counterA[ord(char) - ord("a")] += 1 
        
        for char in b: 
            counterB[ord(char) - ord("a")] += 1 
            
        ans = m - max(counterA) + n - max(counterB)
        
        for i in range(25):
            counterA[i + 1] += counterA[i]
            counterB[i + 1] += counterB[i]
            
            ans = min(ans, counterA[i] + n - counterB[i])
            ans = min(ans, m - counterA[i] + counterB[i])
            
        return ans
