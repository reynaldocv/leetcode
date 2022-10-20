# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        tmp = {}
        tmp[0] = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tmp[1] = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        tmp[2] = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tmp[3] = ["", "M", "MM", "MMM"]
        
        idx = 0
        
        ans = ""
        
        while num: 
            unit = num % 10
            
            ans = tmp[idx][unit] + ans
            
            num //= 10 
            idx += 1 
            
        return ans 
            
