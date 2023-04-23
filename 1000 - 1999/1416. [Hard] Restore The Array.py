# https://leetcode.com/problems/restore-the-array/

class Solution:
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
