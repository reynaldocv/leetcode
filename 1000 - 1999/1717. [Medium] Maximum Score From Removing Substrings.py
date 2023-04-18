# https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def helper(arr, prev, letter, gain):
            stack = []
            
            ans = 0 
            
            for char in arr: 
                if char == letter:
                    if stack and stack[-1] == prev:
                        stack.pop() 

                        ans += gain

                    else: 
                        stack.append(char)

                else: 
                    stack.append(char)
                    
            return ans, stack
            
        if y > x: 
            s = s[:: -1]
            
            x, y = y, x 
            
        gainAB, stack = helper(s, "a", "b", x)
        gainBA, _ = helper(stack, "b", "a", y)
        
        return gainAB + gainBA
        
