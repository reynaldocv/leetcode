# https://leetcode.com/problems/minimum-moves-to-convert-string/

class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = 0 
        idx, n = 0, len(s) 
        while idx < n: 
            if s[idx] == "X":
                idx += 3
                ans += 1
            else: 
                idx += 1
        
        return ans
        
