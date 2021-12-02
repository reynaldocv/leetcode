# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        q = n // 7
        r = n % 7
        ans = 0
        for i in range(q):
            ans += (7 + i)*(7 + i + 1)//2 - i*(i + 1)//2
       
        for i in range(r):
            ans += (i + 1) + q
       
        return ans
        
