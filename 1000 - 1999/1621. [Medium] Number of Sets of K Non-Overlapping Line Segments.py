# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:   
        MOD = 10**9 + 7
        
        ans = 1
        for i in range(1, k * 2 + 1):
            ans *= n + k - i
            ans //= i
            
        return ans % MOD
        
class Solution2:
    def numberOfSets(self, n: int, k: int) -> int:      
        MOD = 10**9 + 7
        dp = [[0] * k for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = i * (i + 1) // 2
            
        for j in range(k):
            dp[j + 1][j] = 1
            
        for j in range(1, k):
            temp = 0
            for i in range(j + 1, n):
                dp[i][j] = dp[i - 1][j]
                temp += dp[i - 1][j - 1]
                dp[i][j] += temp
                dp[i][j] %= MOD
                
        return dp[-1][-1]

class Solution3:
    def numberOfSets(self, n: int, k: int) -> int:
        @cache
        def helper(n, k):    
            if k == 0:
                return 1            
            elif  k > n: 
                return 0 
            else: 
                ans = 0 
                for i in range(1, n + 1):
                    ans += helper(n - i, k - 1)
                    
                ans += helper(n - 1, k)
                
                return ans
        
        MOD = 10**9 + 7
        
        return helper(n - 1, k) % MOD
    
    
