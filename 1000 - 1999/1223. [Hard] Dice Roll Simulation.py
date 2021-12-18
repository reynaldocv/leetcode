# https://leetcode.com/problems/dice-roll-simulation/

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        @cache
        def helper(n, x, r):
            if n == 0: 
                return 1
            
            ans = 0
            
            for i in range(6): 
                if i != x: 
                    ans += helper(n - 1, i, 1)
                    
                elif i == x and r < rollMax[x]: 
                    ans += helper(n - 1, x, r + 1)
                    
            return ans 
        
        MOD = 10**9 + 7        
        ans = 0 
        
        for i in range(6):
            ans += helper(n - 1, i, 1)
            
        return ans % MOD
