# https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        seen = {}
        i = 1
        ans = 0
        while i not in seen: 
            ans += 1
            seen[i] = True
            if i % 2 == 1: 
                i = n//2 + (i - 1)//2
            else:
                i = i//2
                
        return ans
            
        
        
