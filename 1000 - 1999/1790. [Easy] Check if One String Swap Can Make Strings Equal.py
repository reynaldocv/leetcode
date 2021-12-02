# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n != m: return False
        dic = {}
        for i in range(n):
            dic[s1[i]] = dic.get(s1[i], 0) + 1
        
        for i in range(n):
            if s2[i] in dic:
                dic[s2[i]] = dic.get(s2[i], 0) - 1
                if dic[s2[i]] < 0:
                    return False
            else: 
                return False
        
        ans = 0
        for i in range(n):
            if s1[i] != s2[i]:
                ans += 1
        
        return (ans == 0 or ans == 2)
