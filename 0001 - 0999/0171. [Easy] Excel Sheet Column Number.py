# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = {chr(ord("A") + i): i + 1 for i in range(26)}
        
        base = 1 
        
        ans = 0 
        
        for char in columnTitle[:: - 1]:
            ans += num[char]*base 
            
            base *= 26
            
        return ans 
            
