# https://leetcode.com/problems/clumsy-factorial/

class Solution:
    def clumsy(self, n: int) -> int:
        def helper(sign, num):
            if num >= 4: 
                tmp = sign*num*(num - 1)/(num - 2) + (num - 3)
                
            elif num == 3: 
                tmp = sign*num*(num - 1)/(num - 2)
                
            elif num == 2: 
                tmp = sign*num*(num - 1)
                
            elif num == 1: 
                tmp = sign*num 
                
            else:
                tmp = 0 
                
            return int(tmp)
            
        ans = helper(1, n)
        
        n -= 4 
        
        while n > 0: 
            ans += helper(-1, n)
            
            n -= 4 
            
        return ans
            
        
