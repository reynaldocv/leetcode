# https://leetcode.com/problems/shortest-palindrome/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        ans = (inf, "")        
        n = len(s)
        for i in range(1, n + 1):
            newWord = s[:i]
            if newWord == newWord[::-1]:
                ans = min(ans, (n - len(newWord), s[i:][::-1] + s))
                
        return ans[1]
        
