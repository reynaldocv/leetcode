# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        @cache 
        def helper(i, j, mask):
            if j == n: 
                return 1
            if i == m: 
                return helper(0, j + 1, mask)
            
            ans = 0 
            for x in [1 << 2*i, 1 << 2*i + 1, 0b11 << 2*i]:
                aux = mask ^ x
                if aux & (0b11 << 2*i): 
                    if (i == 0 or (aux >> 2*i) & 0b11 != (aux >> 2*i - 2) & 0b11):
                        ans += helper(i + 1, j, aux)
            
            return ans % MOD
            
        MOD = 10**9 + 7
        
        return helper(0, 0, 0)
        
