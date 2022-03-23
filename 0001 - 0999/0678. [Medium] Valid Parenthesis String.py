# https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '(*':
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)

        stars = []
        parens = []

        for (i, c) in enumerate(stack):
            if c == "*":
                stars.append((i, c))
            elif c == '(':
                parens.append((i, c))
            else: 
                if parens:
                    parens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        while parens:
            (i, c) = parens.pop()
            if not stars:
                return False
            if stars[-1][0] < i:
                return False
            stars.pop()        

        return True
