# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s) 
        
        seen = defaultdict(lambda: -1)        
        seen[0] = -1
        
        cnt = 0
        
        ans = 1 
        
        for i in range(1, n):
            if s[i - 1] == s[i]:
                cnt += 1 
            
            ans = max(ans, i - seen[cnt - 1])
            
            if cnt not in seen: 
                seen[cnt] = i - 1
            
        return ans 
        
        
