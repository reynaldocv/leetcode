# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        others = {}
        for i in range(26):
            others[chr(ord("a") + i)] = chr(ord("A") + i)
            others[chr(ord("A") + i)] = chr(ord("a") + i)
            
        stack = []
        
        for char in s: 
            if stack and stack[-1] == others[char]:
                stack.pop() 
            
            else: 
                stack.append(char)
                
        return "".join(stack)
        
