# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen = {(0, 0, 0, 0, 0): -1}
        
        cnt = (0, )*5
        
        index = {char: i for (i, char) in enumerate("aeiou")}
        
        ans = 0 
        
        for (i, char) in enumerate(s): 
            if char in "aeiou":
                idx = index[char]
                
                cnt = cnt[: idx] + ((cnt[idx] + 1) % 2, ) + cnt[idx + 1: ]
                
            if cnt in seen: 
                ans = max(ans, i - seen[cnt])

            else: 
                seen[cnt] = i 
                    
        return ans 
                    
        
