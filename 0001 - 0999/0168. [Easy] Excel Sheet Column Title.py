# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dic = {i + 1: chr(i + ord("A")) for i in range(0, 26)}
        print(dic)
        ans, n = "", columnNumber 
        while (n > 0):
            r = (n % 26) 
            n = n // 26
            if r == 0:
                r = 26
                n -= 1  
            ans = dic[r] + ans
        return ans
            

    
