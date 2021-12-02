# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ind = 0
        l = len(S)
        ans = ""
        for i in S:
            ind = ind + 1 if (i == "(") else ind - 1
            if not ((ind == 1 and i=="(") or (ind == 0 and i==")")):
                ans += i                
        return ans
            
