# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        
        for char in s: 
            if char == "[":
                stack.append(char)
                
            else: 
                if stack and stack[-1] == "[":
                    stack.pop() 
                    
                else: 
                    stack.append("]")
                    
        n = len(stack)//2
        
        return (n + 1)//2
        
