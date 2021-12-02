# https://leetcode.com/problems/perfect-number/

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        n = int(num**0.5)        
        divisors = set([1])
        for i in range(2, n + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num//i)

        return num == sum(divisors)
        
        
