# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        a = []
        ans = 0
        aux = 0
        for i in range(len(s)):
            if s[i] == "(":
                a.append("(")
                ans = max(ans, len(a))
            if s[i] == ")":
                a.pop()
        if len(a) == 0:
            return ans
