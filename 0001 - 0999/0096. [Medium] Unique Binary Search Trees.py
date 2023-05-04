# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def helper(num):
            if num <= 1: 
                return 1 
            
            else: 
                ans = 0 
                
                for i in range(0, num):
                    ans += helper(i)*helper(num - 1 - i)
                    
                return ans 
            
        return helper(n)
        
class Solution2:
    def numTrees(self, n: int) -> int:
        dp = [1] + [0 for _ in range(n)]
        
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j]*dp[i - 1 - j]
                
        return dp[-1]
