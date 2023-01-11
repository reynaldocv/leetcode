# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = [chr(ord("A") + i) for i in range(26)]
        
        ans = ""
        
        while columnNumber > 0:
            ans += letters[(columnNumber - 1) % 26]
            
            columnNumber = (columnNumber - 1)//26
            
        return ans[:: -1]
        
        
