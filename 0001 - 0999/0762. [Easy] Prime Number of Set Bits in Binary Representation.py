# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def counter1(num):
            ans = 0
            while num > 0:
                ans = ans + 1 if (num % 2 == 1) else ans
                num = num // 2
            return ans
        
        def isPrime(num):
            if (num == 1):
                return False
            
            aux = int(num**(.5))
            ans = True
            for i in range(2, aux + 1):
                if num % i == 0:
                    ans = False
                    break
            return ans
        
        ans = 0
        for i in range(L, R + 1):
            if isPrime(counter1(i)):
                ans += 1
        return ans
