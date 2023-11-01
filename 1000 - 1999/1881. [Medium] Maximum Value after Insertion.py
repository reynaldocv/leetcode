# https://leetcode.com/problems/maximum-value-after-insertion/

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        sign = "" 
        
        if n[0] == "-":
            sign = "-"
            n = n[1: ]
        
        start = 0 
        x = str(x)
        
        m = len(n)
        
        if sign == "":         
            while start < m and  n[start] >= x:
                start += 1 
                
        else: 
            while start < m and n[start] <= x:
                start += 1
        
        return sign + n[: start] + x + n[start: ]
                
                

            
      
