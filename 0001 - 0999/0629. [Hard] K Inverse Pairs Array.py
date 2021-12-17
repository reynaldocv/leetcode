# https://leetcode.com/problems/k-inverse-pairs-array/

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @cache
        def helper(n, k):
            if n == 0: 
                return 0 
            
            if k == 0: 
                return 1
            
            if k - n >= 0: 
                val = helper(n - 1, k) - helper(n - 1, k - n)
            else: 
                val = helper(n - 1, k) 
                
            return helper(n, k - 1) + val 
            
        MOD = 10**9 + 7
        
        if k > 0: 
            return (helper(n, k) - helper(n, k - 1)) % MOD
        else: 
            return helper(n, k) % MOD
