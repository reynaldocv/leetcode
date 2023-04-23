# https://leetcode.com/problems/restore-the-array/

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        
        m, n = len(s), len(str(k))
        
        dp = [1] + [0 for _ in range(m)]
        
        for i in range(1, m + 1):
            tmp = ""
            j = i 
            
            ans = 0 
            
            while j >= 0 and len(tmp) <= n: 
                tmp = s[j - 1] + tmp 
                
                if s[j - 1] != "0":
                    if int(tmp) <= k: 
                        ans += (dp[j - 1] % MOD)
                        
                    else: 
                        break 
                        
                j -= 1 
        
            dp[i] = ans % MOD
        
        return dp[-1] % MOD
    
class Solution2:
    def numberOfArrays(self, s: str, k: int) -> int:
        @cache 
        def helper(i):
            if i == n: 
                return 1 
            
            else: 
                ans = 0                 
                tmp = ""
                
                if s[i] != "0":                
                    for j in range(i, n):
                        tmp += s[j] 
                        
                        if int(tmp) <= k: 
                            ans += helper(j + 1) % MOD
                            
                        else: 
                            break 
                            
                return ans
            
        MOD = 10**9 + 7
                    
        n = len(s)
        
        return helper(0) % MOD
