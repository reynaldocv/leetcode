# https://leetcode.com/problems/number-of-ways-to-split-a-string/

class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7
        ones = []
        
        for (i, char) in enumerate(s):
            if char == "1":
                ones.append(i)
                
        n = len(s)
        
        m = len(ones)        
        
        if m % 3 != 0: 
            ans = 0 
        
        elif m == 0: 
            ans = (n - 1)*(n - 2)//2
          
        else:
            q = m//3 

            ans = (ones[q] - ones[q - 1])*(ones[2*q] - ones[2*q - 1])
            
        return ans % MOD

        
