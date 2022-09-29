# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mult = 1
        aSum = 0

        for char in str(n):
            mult *= int(char)
            aSum += int(char)

        return mult - aSum  
                
