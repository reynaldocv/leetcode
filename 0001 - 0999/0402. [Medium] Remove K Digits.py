# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        
        if n == k: 
            return "0"
        
        stack = []
        
        for (i, digit) in enumerate(num):
            while stack and stack[-1] > digit and len(stack) + n - i > n - k:
                stack.pop() 
             
            if len(stack) < n - k: 
                stack.append(digit)
                
        while stack and stack[0] == "0":
            stack.pop(0)
            
        if stack:             
            return "".join(stack) 
        
        return "0"
               
