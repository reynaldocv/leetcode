# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aSum = int(a, 2) + int(b, 2)
        
        ans = ""
        
        if aSum == 0: 
            return "0"
        
        while aSum > 0: 
            ans += str(aSum % 2)
            aSum //= 2 
        
        return ans[:: -1] 
