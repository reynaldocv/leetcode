# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        
        right = [0 for i in range(n)]
        cnt = 0
        for i in range(n - 1, -1, -1):
            cnt += 1 if s[i] == "a" else 0 
            right[i] = cnt
            
        ans = min(cnt, n - cnt)
        
        left = 0 
        for i in range(n):
            ans = min(ans, left + right[i])
            left += 1 if s[i] == "b" else 0
            
        return ans
        
