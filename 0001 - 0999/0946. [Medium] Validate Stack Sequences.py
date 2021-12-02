# https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        i, j = 0, 0
        
        stack = []
        
        while i < n and j < n: 
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else: 
                stack.append(pushed[i])
                i += 1
                
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
        return not stack
        
        

        
