# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("(al)", "al")
        command = command.replace("()", "o")
        return command
        
class Solution2:
    def interpret(self, command: str) -> str:
        stack = []
        
        for char in command: 
            if char == ")":
                if stack[-1] == "(":
                    stack.pop()
                    stack.append("o")
                else: 
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append("al")
                    
            else: 
                stack.append(char)

        return "".join(stack)
                
