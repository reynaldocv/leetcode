# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        
        ans = "0"
        
        for i in range(n):
            if number[i] == digit:
                ans = max(ans, number[: i] + number[i + 1: ])
            
        return ans 
            
