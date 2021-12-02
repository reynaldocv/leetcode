# https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        num, den = numerator, denominator
        
        sign = -1 if num < 0 else 1
        sign = sign*-1 if den < 0 else sign
        
        num = abs(num)
        den = abs(den)
        
        if num == 0: 
            return "0"
        
        ans = str(num//den)
        num = num % den
        
        if num == 0: 
            return "-" + ans if sign == -1 else ans
        else: 
            quo = []
            idx = 0
            seen = {}            
            while num != 0 and num not in seen: 
                seen[num] = idx
                idx += 1
                num *= 10 
                quo.append(str(num // den))
                num %= den
            
            if num == 0: 
                ans += "." + "".join(quo)
            else: 
                ans += "." + "".join(quo[:seen[num]]) + "(" + "".join(quo[seen[num]:]) + ")"  
                
            return "-" + ans if sign == -1 else ans
        
       
