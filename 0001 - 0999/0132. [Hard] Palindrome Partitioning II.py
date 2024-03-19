# https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def helper(start):
            if start == n:
                return 0 
            
            else: 
                ans = n - start
                
                for i in range(start + 1, n + 1):
                    tmp = s[start: i]
                    
                    if tmp == tmp[:: -1]:
                        ans = min(ans, 1 + helper(i))
                        
                return ans 
            
        n = len(s)
            
        return helper(0) - 1

class Solution2:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        dp = defaultdict(lambda: inf)        
        dp[-1] = 0 
        
        for end in range(n):
            for start in range(end, -1, -1):
                word = s[start: end + 1]
                
                if word == word[:: -1]:
                    dp[end] = min(dp[end], dp[start - 1] + 1)
    
        return dp[n - 1] - 1
        
            
        
