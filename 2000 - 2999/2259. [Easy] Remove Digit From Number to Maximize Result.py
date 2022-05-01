# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0 
        for (i, char) in enumerate(number):
            if char == digit: 
                ans = max(ans, int(number[: i] + number[i + 1: ]))
                
        return str(ans)
        
