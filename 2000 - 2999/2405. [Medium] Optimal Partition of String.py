# https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        
        ans = 1
        
        for char in s:
            if char in seen:
                ans += 1
                
                seen = set()
            
            seen.add(char)
                
        return ans
        
