# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        def helper(word):
            for char in word: 
                if char not in "0123456789":
                    return False 
                
            return True 
        
        stack = []
        
        for char in s: 
            if heper(char):
                if stack and helper(stack[-1]):
                    num = stack.pop() 

                    stack.append(num + char)
                    
                else:
                    stack.append(char)
                    
            elif char == "[":
                stack.append(char)
                
            elif char == "]":
                tmp = ""
                
                while stack[-1] != "[":
                    tmp = stack.pop() + tmp
                    
                stack.pop()
                
                num = int(stack.pop())
                
                stack.append(num*tmp)
                
            else: 
                stack.append(char)
                
        return "".join(stack)
                    
        
