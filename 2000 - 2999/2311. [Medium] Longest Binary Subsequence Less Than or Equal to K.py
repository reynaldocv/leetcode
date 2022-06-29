# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:         
        ans = val = 0 
        
        for (i, char) in enumerate(s[:: -1]): 
            if char == '0': 
                ans += 1
                
            elif val + (1 << i) <= k:                
                ans += 1
                val += (1 << i)
                
        return ans 
