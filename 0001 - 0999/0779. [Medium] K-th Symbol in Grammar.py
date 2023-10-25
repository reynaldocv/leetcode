# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = 0 
        
        k = k - 1
        
        while n > 0: 
            if k >= 2**(n - 1):
                k %= 2**(n - 1)
                
                ans = 1 - ans
                
            n -= 1 
            
        return ans
        
