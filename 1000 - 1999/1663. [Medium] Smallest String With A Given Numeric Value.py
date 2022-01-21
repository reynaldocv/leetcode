# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        def helper(n, val):
            if (n - 1)*26 >= val: 
                return "a" + helper(n - 1, val - 1)
            else: 
                return chr(ord("a") + ((val - 1) % 26)) + "z"*(n - 1)
            
        return helper(n, k)
                
                
        
        
        
