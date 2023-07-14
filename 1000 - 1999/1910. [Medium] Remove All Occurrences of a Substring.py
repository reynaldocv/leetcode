# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part) 
        
        stack = []
        
        for char in s: 
            stack.append(char)
            
            if len(stack) >= n and char == part[-1]: 
                if "".join(stack[-n: ]) == part: 
                    for _ in range(n):
                        stack.pop()
                        
        return "".join(stack)
            
        
                
        
        
