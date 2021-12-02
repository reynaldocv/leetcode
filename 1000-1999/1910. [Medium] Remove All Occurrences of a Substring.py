# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m = len(part)
        letter = part[-1]
        stack = []
        for char in s: 
            stack.append(char)
            if char == letter: 
                if len(stack) >= m:
                    if "".join(stack[len(stack) - m:]) == part: 
                        for i in range(m):
                            stack.pop()
        
        return "".join(stack)
                    
                
        
        
