# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = defaultdict(lambda: -1)
        
        start = -1 
        
        ans = 0 
        
        for (i, char) in enumerate(s):
            start = max(start, last[char])
            
            ans = max(ans, i - start)
            
            last[char] = i       
            
        return ans 
            
