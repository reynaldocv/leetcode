# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        _mul = 1; 
        _sum = 0; 
        while n > 0:
            dig = n % 10
            _mul *= dig
            _sum += dig
            n = n//10
        return _mul - _sum
                
