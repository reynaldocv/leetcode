# https://leetcode.com/problems/convert-to-base-2/

class Solution:
    def baseNeg2(self, n: int) -> str:
        ans = ""
        if n == 0:
            return "0"
        
        while n != 0:
            print(n, ans)
            if n % 2 != 0:
                ans = "1" + ans
                n = (n - 1)//-2
            else:
                ans = "0" + ans
                n = n//-2
        
        return ans
        
