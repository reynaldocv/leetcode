# https://leetcode.com/problems/sum-of-scores-of-built-strings/

class Solution:
    def sumScores(self, s: str) -> int:
        def helper(s):
            dp = [0 for _ in range(n)]
            left, right = 0, 0
            
            for i in range (1, n):
                if i > right:
                    left = right = i
                    
                    while right < n and s[right - left] == s[right]:
                        right += 1
                    right -= 1
                    
                    dp[i] = right - left + 1
                else:
                    val = i - left
                    
                    if dp[val] + i <= right:
                        dp[i] = dp[val]
                        
                    else:
                        left = i
                        
                        while right < n and s[right - left] == s[right]:
                            right += 1
                        right -= 1
                        
                        dp[i] = right - left + 1
                        
            return sum(dp)
        
        n = len(s)
        
        return helper(s) + n
