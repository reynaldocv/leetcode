# https://leetcode.com/problems/monotone-increasing-digits/

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        strN = str(n)
        m = len(strN)
        nums = [char for char in strN] 
        
        stack = []
        
        for (i, char) in enumerate(nums): 
            while stack and stack[-1] > char: 
                char = str(int(stack.pop()) - 1)
                
            stack.append(char) 
            
            if len(stack) <= i: 
                break 
                
        return int("".join(stack) + "9"*(m - len(stack)))
        
        
        
        
        
