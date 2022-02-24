# https://leetcode.com/problems/knight-dialer/

class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        
        next = {}
        next[1] = [6, 8]
        next[2] = [7, 9]
        next[3] = [4, 8]
        next[4] = [3, 9, 0]
        next[5] = []
        next[6] = [0, 1, 7]
        next[7] = [6, 2]
        next[8] = [1, 3]
        next[9] = [2, 4]
        next[0] = [4, 6]
        
        dp = [1 for _ in range(10)]
        
        for _ in range(n - 1):
            dp2 = [0 for _ in range(10)]
            for i in range(10):
                for k in next[i]:
                    dp2[k] += dp[i] % MOD
            
            dp = dp2
            
        return sum(dp) % MOD  
