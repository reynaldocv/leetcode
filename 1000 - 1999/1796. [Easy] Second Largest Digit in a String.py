# https://leetcode.com/problems/second-largest-digit-in-a-string/

class Solution:
    def secondHighest(self, s: str) -> int:
        dic, n = {},  len(s)
        for i in range(n):
            if s[i] in "1234567890":
                dic[int(s[i])] = True
        if len(dic) <= 1: 
            return -1
        else: 
            ans = [*dic]
            ans.sort(reverse = True)
            return ans[1]
        
