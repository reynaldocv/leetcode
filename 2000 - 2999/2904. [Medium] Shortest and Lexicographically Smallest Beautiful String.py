# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = (inf, "")
        
        last = {0: -1}
        
        prev = 0 
        
        for (i, char) in enumerate(s):
            if char == "1":
                prev += 1 
                
            if prev >= k: 
                ans = min(ans, (i - last[prev - k], s[last[prev - k] + 1: i + 1]))
                
            last[prev] = i 

        return ans[1]
