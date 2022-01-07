# https://leetcode.com/problems/student-attendance-record-ii/

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1, 2, 4]
        for i in range(3, n + 1): 
            dp.append((dp[i - 3] + dp[i - 2] + dp[i - 1]) % MOD)
        
        ans = dp[n] 
        
        for i in range(n): 
            ans = (ans + dp[i]*dp[n - 1 - i]) % MOD
        
        return ans

class Solution2: #Memory Limit Exceeded
    def checkRecord(self, n: int) -> int:
        @cache 
        def helper(i, absent, late): 
            if i == n: 
                return 1
            
            ans = helper(i + 1, absent, 0) 
            
            if absent == 0: 
                ans += helper(i + 1, 1, 0)
                
            if late < 2: 
                ans += helper(i + 1, absent, late + 1)  
            
            return ans % MOD
        
        MOD = 10**9 + 7
        
        return helper(0, 0, 0)
