# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        letters = {str(i + 1) + "#": chr(ord("a") + i) for i in range(9, 26)}
        
        for i in range(1, 10):
            letters[str(i)] = chr(ord("a") + i - 1)
        
        stack = []
        
        for char in s: 
            if char == "#":
                second = stack.pop() 
                first = stack.pop() 
                
                stack.append(letters[first + second + "#"])
                
            else: 
                stack.append(char)
                
        for (i, elem) in enumerate(stack): 
            if elem in "123456789":
                stack[i] = letters[elem]
                
        return "".join(stack)
