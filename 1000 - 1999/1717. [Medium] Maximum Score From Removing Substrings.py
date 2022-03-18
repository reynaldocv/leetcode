# https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        val1, val2 = "a", "b"
        
        if x > y: 
            x, y, val1, val2 = y, x, val2, val1
            
        stack = []
        ans = 0 
        
        for _ in range(2):
            for char in s: 
                if stack and char == val1 and stack[-1] == val2: 
                    stack.pop()
                    ans += y                
                else: 
                    stack.append(char)
                    
            s = "".join(stack)
            x, y, val1, val2 = y, x, val2, val1
            stack = []
            
        return ans
