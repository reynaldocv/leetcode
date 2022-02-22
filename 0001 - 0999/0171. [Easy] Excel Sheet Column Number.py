# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        values = {chr(ord("A") + i): i + 1 for i in range(26)}
        ans = 0 
        p = 1
        
        for char in columnTitle[::-1]:
            ans += p*values[char]
            p *= 26
            
        return ans
            
