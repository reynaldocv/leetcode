# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        for char in s: 
            seen[char] = True
            
        ans = 0            
        for key in seen:             
            idx = {}
            flips = 0
            for (i, char) in enumerate(s):
                if char != key: 
                    flips += 1                    
                    idx[flips] = i
                    
                start = idx[flips - k] if flips > k else -1
                ans = max(ans, i - start)
                
        return ans
                    
                    
