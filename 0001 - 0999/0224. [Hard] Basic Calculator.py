# https://leetcode.com/problems/basic-calculator/

 class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        sign = 1
        stack = []
        num = 0 
        for char in s + "+": 
            if char.isdigit(): 
                num = (num * 10) + int(char)
            elif char in "+-":
                ans += sign*num                
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append(ans)
                stack.append(sign)                
                sign, ans = 1, 0
            elif char == ")":
                ans += sign*num
                ans *= stack.pop()
                ans += stack.pop()
                num = 0
        return ans
                
            
