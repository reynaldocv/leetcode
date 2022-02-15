# https://leetcode.com/problems/bag-of-tokens/

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        stack = tokens.copy()
        ans = bns = 0
        
        while stack and (power >= stack[0] or bns):
            while stack and power >= stack[0]:
                power -= stack.pop(0)
                bns += 1
                
            ans = max(ans, bns)
            
            if stack and bns: 
                power += stack.pop()
                bns -= 1 
                
        return ans
            
