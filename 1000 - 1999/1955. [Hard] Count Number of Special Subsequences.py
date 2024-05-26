# https://leetcode.com/problems/count-number-of-special-subsequences/

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        s0 = s1 = s2 = 0 
        
        for num in nums: 
            if num == 0: 
                s0 = (1 + 2*s0) % MOD
                
            elif num == 1: 
                s1 = (s0 + 2*s1) % MOD
                
            else: 
                s2 = (s1 + 2*s2) % MOD
                
        return s2
        
