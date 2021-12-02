# https://leetcode.com/problems/base-7/

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        sign = "-" if num < 0 else ""
        num = -1*num if num < 0 else num   
        ans = ""
        while (num > 0):
            r = num % 7
            num = num//7
            ans = str(r) + ans
        
        return sign + ans
            
