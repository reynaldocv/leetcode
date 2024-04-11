# https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        values = {chr(ord("a") + i): i + 1 for i in range(26)}
        
        for (ith, char) in enumerate(chars):
            values[char] = vals[ith]
            
        ans = prev = 0 
        
        for char in s: 
            prev = max(0, prev + values[char])
            
            ans = max(ans, prev)
            
        return ans 
        
