# https://leetcode.com/problems/substring-with-largest-variance/

class Solution:
    def largestVariance(self, s: str) -> int:
        def helper(a, b):
            ans = 0 
            seen = set()
            prefix = 0 
            for char in s: 
                if char == a: 
                    prefix += 1 
                    seen.add(a)
                elif char == b:
                    prefix -= 1 
                    seen.add(b)
                    
                if prefix < 0: 
                    prefix = 0 
                    seen = set()
                    
                if len(seen) == 2: 
                    ans = max(ans, prefix)
                    
            if len(seen) == 1: 
                ans = max(ans, prefix - 1)
                    
            return ans
                
        chars = set([char for char in s])
                
        ans = 0         
        
        for char1 in chars:
            for char2 in chars: 
                if char1 != char2:
                    ans = max(ans, helper(char1, char2))
                    
        return ans 
                
                
        
