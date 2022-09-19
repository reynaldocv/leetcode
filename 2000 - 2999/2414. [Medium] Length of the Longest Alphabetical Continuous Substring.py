# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        index = {chr(ord("a") + i): i for i in range(26)}
        
        cnt = 1 
        ans = 1
        
        for (i, char) in enumerate(s):
            if i > 0: 
                if index[s[i - 1]] + 1 == index[char]:
                    cnt += 1 
                else: 
                    cnt = 1 
            
            ans = max(ans, cnt)
                
        return ans 
                    
        
