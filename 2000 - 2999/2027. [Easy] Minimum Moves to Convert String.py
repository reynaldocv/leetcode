# https://leetcode.com/problems/minimum-moves-to-convert-string/

class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s) 
        
        i = 0 
        
        ans = 0 
        
        while i < n: 
            if s[i] == "X":
                i += 3
                ans += 1
            else: 
                i+= 1
        
        return ans
        
class Solution2:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        
        dp = defaultdict(lambda: 0)
        
        for (i, char) in enumerate(s):
            if char == "X":
                dp[i] = dp[i - 3] + 1
                
            else: 
                dp[i] = dp[i - 1]
                
        return dp[n - 1]
        
