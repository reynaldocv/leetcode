# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

class Solution:
    def modifyString(self, s: str) -> str:
        letters = ""
        for i in range(ord("a"), ord("z") + 1):
            letters += chr(i)
            
        ans = ""
        n = len(s)
        for i in range(n):
            if s[i] == "?":
                arr = []
                if i - 1 >= 0:
                    arr.append(ans[i - 1])
                if i + 1 < n:
                    arr.append(s[i + 1])
                idx = 0
                while letters[idx] in arr: 
                    idx += 1
                ans += letters[idx]
            else: 
                ans += s[i]
        return ans
