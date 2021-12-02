# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:        
        value = 1
        while n > 0: 
            if 2**(n - 2) < k <= 2**(n - 1):
                k -= 2**(n - 2)
                value = 1 - value 
            n -= 1
        
        return value if value == 0 else 1
            
                
        
        
        https://leetcode.com/problems/k-th-symbol-in-grammar/
