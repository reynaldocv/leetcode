# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0 
        operation = "+"
        for char in s + "+":
            if char == " ":
                continue
            elif char.isdigit():
                cur = (cur * 10) + int(char)
            else:
                if operation == "+":
                    stack.append(cur)
                elif operation == "-":
                    stack.append(-cur)
                elif operation == "*":
                    stack.append(stack.pop() * cur)
                elif operation == "/": 
                    stack.append(int(stack.pop() / cur))
                operation = char
                cur = 0 
                
        return sum(stack)
            
            
            
