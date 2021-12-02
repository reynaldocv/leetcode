# https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        j = -1
        for i in range(n - 1, -1, -1):
            if int(num[i]) % 2 == 1: 
                j = i
                break
        
        return "" if j == -1 else num[:j + 1]
        
    
        
        
