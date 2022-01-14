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

class Solution2:
    def myAtoi(self, s: str) -> int:
        n = len(s)        
        i, state = 0, 0
        
        while i < n and state < 3:            
            if state == 0: 
                if s[i].isdigit():
                    state = 2
                elif s[i] == "+" or s[i] == "-":
                    state = 1
                elif s[i] == " ":
                    state = 0
                else: 
                    state = 3
            elif state == 1: 
                if s[i].isdigit():
                    state = 2
                else: 
                    state = 3
            elif state == 2: 
                if s[i].isdigit():
                    state = 2
                else:
                    state = 4            
            i += 1
            
        if state == 3 or state == 0 or state == 1: 
            return 0
        else:             
            if state == 4: 
                aux = s[: i - 1]
            elif state == 2:
                aux = s[: i                       ]
            aux.replace(" ", "")
            ans = int(aux)
            
            if ans < -2**31:
                ans = -2**31
            elif ans > 2**31 - 1:
                ans = 2**31 - 1
            return ans
       
