# https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        num = pow(2, a) * pow(2, b)        
        return 0 if num == 1 else int(log(num, 2))
        
