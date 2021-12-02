# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        if n < m:
            num1, num2 = num2, num1
            n, m = m, n
        q = 0
        ans = ""
        for i in range(0, m):
            aux = int(num1[n - i - 1]) + int(num2[m - i - 1]) + q
            q = aux//10
            r = aux % 10
            ans = str(r) + ans
        print(ans)
        for i in range(n - m - 1, -1, -1):
            aux = int(num1[i]) + q
            q = aux//10
            r = aux % 10
            ans = str(r) + ans
        print(ans)        
        if q == 1:
            ans = "1" + ans
        print(ans)
        
        return ans            
            
