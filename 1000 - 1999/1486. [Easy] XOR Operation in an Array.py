# https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0 
        
        for i in range(n):
            ans ^= (start + 2*i)
            
        return ans 
        
              
