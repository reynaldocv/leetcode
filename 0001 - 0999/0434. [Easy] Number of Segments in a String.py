# https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution:
    def countSegments(self, s: str) -> int:
        if s == "": return 0
        n, ans, aux = len(s), 0, ""
        for i in range(n):
            if s[i] == " ":                
                if len(aux) != 0: 
                    ans += 1
                aux = ""
            else:
                aux += s[i]
        if aux != "":
            ans += 1
        return ans
            
            
