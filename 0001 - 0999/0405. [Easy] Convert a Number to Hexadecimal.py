# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        
        val = {i: str(i) for i in range(10)}
        for i in range(6):
            val[i + 10] = chr(i + ord("a"))
        if num < 0: 
            num += 2**32
        ans = ""
        while num > 0: 
            r = num % 16
            ans = val[r] + ans
            num = num // 16
        
        return ans
