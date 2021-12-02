# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquareDigits(n):
            if n <= 1: return 1
            ans = 0
            while n > 0:
                ans += (n % 10)**2
                n = n // 10
            return ans
        
        dic = {}        
        while n != 1 and n not in dic:
            dic[n] = True
            n = sumOfSquareDigits(n)
        
        return True if n == 1 else False
        
        
