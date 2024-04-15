# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(nth, k):            
            if nth == 1: 
                return 0 
            
            elif 0 <= k < 2**(nth - 1):
                return helper(nth - 1, k)
            
            elif k == 2**(nth - 1): 
                return 1 
            
            else: 
                k %= (2**(nth - 1))
                
                k = 2**(nth - 1) - k
                
                return 1 - helper(nth - 1, k)
            
        return str(helper(n, k))
                
        
        
                
