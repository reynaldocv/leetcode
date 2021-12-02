# https://leetcode.com/problems/maximum-value-after-insertion/

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        
        l = len(n)
        if n[0] == "-":
            for i in range(1, l):
                if n[i] <= str(x):
                    continue
                else: 
                    return n[:i] + str(x) + n[i:]
                
            return n + str(x)
            
        else: 
            for i in range(l):
                if n[i] >= str(x):
                    continue
                else: 
                    return n[:i] + str(x) + n[i:]
                
            return n + str(x)
            
      
