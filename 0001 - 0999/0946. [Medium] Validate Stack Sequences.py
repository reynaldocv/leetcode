# https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
   
        while pushed: 
            while stack and popped and stack[-1] == popped[0]: 
                stack.pop()
                popped.pop(0)
            
            if pushed:             
                stack.append(pushed.pop(0))
         
        while stack and popped and stack[-1] == popped[0]: 
            stack.pop()
            popped.pop(0)
                
        return len(stack) == 0

class Solution2:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        
        pushed += "$"
   
        while pushed: 
            while stack and popped and stack[-1] == popped[0]: 
                stack.pop()
                popped.pop(0)
            
            if pushed:             
                stack.append(pushed.pop(0))
         
        return len(stack) == 1
        
        

        
