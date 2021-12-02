# https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for char in s: 
            if char == ")":
                aSum = 0
                while stack and stack[-1] != "(":
                    aSum += stack.pop()
                
                stack.pop()        
                
                if aSum == 0: 
                    stack.append(1)
                else: 
                    stack.append(2*aSum)
            else: 
                stack.append("(")
        
        return sum(stack)
        
        
