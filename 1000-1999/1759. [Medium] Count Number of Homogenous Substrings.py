# https://leetcode.com/problems/count-number-of-homogenous-substrings/

class Solution:
    def countHomogenous(self, s: str) -> int:        
        MOD = 10**9 + 7
        prev = "$"
        cnt = 0
        ans = 0
        for char in s: 
            if char != prev: 
                prev = char
                cnt = 1
            else: 
                cnt += 1
                
            ans = (ans + cnt) % MOD
            
        return ans
        
