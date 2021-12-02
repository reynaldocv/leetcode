# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        aux = []
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] in vowels: 
                aux.append(s[i])
                
        ans, idx = "", 0
        for i in range(0, n):
            if s[i] in vowels:
                ans += aux[idx]
                idx += 1
            else: 
                ans += s[i]
        
        return ans
        
