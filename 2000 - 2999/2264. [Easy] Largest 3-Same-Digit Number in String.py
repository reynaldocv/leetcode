# https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        prev = num[: 2]
        
        for char in num[2: ]:
            prev += char
            if prev[0]*3 == prev:
                ans = max(ans, prev)
                
            prev = prev[1: 3]
            
        return ans
            
        
