# https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution:
    def replaceDigits(self, s: str) -> str:
        l = len(s)
        end = ""
        if l % 2 == 1:
            end = s[l - 1]
        ans = ""
        for i in range(l//2):
            x = 2*i
            y = 2*i + 1
            ans += s[x] + chr(ord(s[x]) + int(s[y]))
        return ans + end
        
        
