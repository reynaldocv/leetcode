# https://leetcode.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = []
        i = 0
        while len(s[i*2*k: (i + 1)*2*k]) > 0:
            arr.append(s[i*2*k: (i + 1)*2*k])
            i += 1
        ans = ""
        for ar in arr:     
            ans += ar[:k][::-1]
            ans += ar[k:2*k]
        return ans
        
