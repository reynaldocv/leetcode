# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0 
        sign = 1
        idx = 0 
        n = len(s)
        
        while idx < n and s[idx] == " ":
            idx += 1 
        
        if idx < n and s[idx] in "+-":
            sign = 1 if s[idx] == "+" else -1
            idx += 1 
            
        while idx < n and s[idx].isdigit():
            ans = ans*10 + int(s[idx])
            idx += 1
            
        if sign*ans > 2**31 - 1: 
            return 2**31 - 1
        
        if sign*ans < -2**31: 
            return -2**31
        
        return sign*ans
