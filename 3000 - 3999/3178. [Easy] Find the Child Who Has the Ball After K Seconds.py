# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        MOD = 2*(n - 1)
        
        k %= MOD 
        
        if k <= n - 1: 
            return k 
        
        else: 
            k %= (n - 1)
            
            return n - k - 1
        
        
        
