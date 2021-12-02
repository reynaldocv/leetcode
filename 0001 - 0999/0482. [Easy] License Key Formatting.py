# https://leetcode.com/problems/license-key-formatting/

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s[::-1]
        s = s.replace("-", "")
        n = len(s)
        aux, ans = "", ""
        for i in range(n):
            aux += s[i].upper()
            if len(aux) == k:
                ans += aux + "-"
                aux = ""
        if len(aux) > 0:
            ans += aux
        else: 
            ans = ans[:len(aux) - 1]
        return ans[::-1]
                
                
