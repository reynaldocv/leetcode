# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = 0
        n = len(s)
        dic = {}
        ans = 0
        for i in range(n):
            start = dic.get(s[i], -1)
            t = min(t + 1, i - start)
            ans = max(ans, t)
            dic[s[i]] = i
        return ans
        
