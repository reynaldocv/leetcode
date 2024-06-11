# https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7        
        
        num = n + k - 1
        den = 1
        
        ans = 1
        
        for _ in range(k):
            ans = (ans * num * pow(den, -1, MOD)) % MOD
            
            num -= 1 
            den += 1
                        
        return ans 
        
