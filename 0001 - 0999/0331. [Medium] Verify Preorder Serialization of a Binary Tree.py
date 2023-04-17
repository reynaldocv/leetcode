# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        arr = preorder.split(",")
        
        stack = []
        
        for char in arr: 
            if char == "#":
                while stack and stack[-1] == "#":
                    stack.pop() 
                    
                    if not stack: 
                        return False 
                    
                    stack.pop() 
                    
                stack.append("#")
                
            else: 
                stack.append(char)
                
        return len(stack) == 1 and stack[0] == "#"
        
