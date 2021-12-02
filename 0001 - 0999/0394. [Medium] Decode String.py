# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        
        for char in s: 
            if char.isdigit():
                if stack and stack[-1].isdigit(): 
                    elem = stack.pop()
                    stack.append(elem + char)
                else: 
                    stack.append(char)
            
            if char.isalpha(): 
                if stack and stack[-1].isalpha(): 
                    elem = stack.pop()
                    stack.append(elem + char)
                else: 
                    stack.append(char)
            
            if char == "[":
                stack.append(char)
            
            if char == "]":                
                word = stack.pop()
                stack.pop()
                num = int(stack.pop())
                newWord = num*word
                if stack and stack[-1].isalpha(): 
                    elem = stack.pop()
                    stack.append(elem + newWord)
                else: 
                    stack.append(newWord)
                
        return stack.pop()        
        
        
