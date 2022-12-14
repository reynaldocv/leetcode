# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0 
        
        for string in strs: 
            if string.isdigit():
                ans = max(ans, int(string))
                
            else: 
                ans = max(ans, len(string))
                
        return ans 
                
