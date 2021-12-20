# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        idx = {char: i for (i, char) in enumerate("aeiou")}
        mask = 0 
        seen = {mask: -1}
        ans = 0 
        for (i, char) in enumerate(s): 
            if char in "aeiou":                
                mask = mask ^ (1 << idx[char])
            if mask in seen: 
                ans = max(ans, i - seen[mask])
            else: 
                seen[mask] = i
                
        return ans
