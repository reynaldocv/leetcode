# https://leetcode.com/problems/number-of-ways-to-split-a-string/

class Solution:
    def numWays(self, s: str) -> int:
        MOD =  10**9 + 7
        
        idx = []
        for (i, char) in enumerate(s): 
            if char == "1":
                idx.append(i)
                
        if len(idx) % 3 != 0: 
            return 0 
        
        n = len(idx)
        
        if n == 0: 
            m = len(s)
            ans = (m - 2)*(m - 1)//2
        
        else:             
            quo = len(idx) // 3
            ans = 1
            for i in range(quo - 1, n - 1, quo):
                ans *= idx[i + 1] - idx[i]

        return ans % MOD 

        
