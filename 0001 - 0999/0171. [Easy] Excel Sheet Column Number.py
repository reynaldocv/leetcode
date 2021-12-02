# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dic = {chr(i): i - ord("A") + 1 for i in range(ord("A"), ord("Z") + 1)}
        n = len(columnTitle) - 1
        ans = 0
        for i in columnTitle: 
            ans += dic[i]*26**(n)
            n -= 1
        return ans
