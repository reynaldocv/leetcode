# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        
        start = 0         
        num = 0 
        
        while start < n and s[start] == " ":
            start += 1 
            
        sign = 1 
        
        if start < n and s[start] in "-+":
            sign = 1 if s[start] == "+" else -1 
            
            start += 1 
            
        
        while start < n and s[start] in "0987654321":
            num = 10*num + int(s[start])
            
            start += 1 
            
        ans = sign*num
        
        if ans < -(2**31):
            return -(2**31)
        
        elif ans >= 2**31:
            return 2**31 - 1
        
        else: 
            return ans 
        
