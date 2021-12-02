# https://leetcode.com/problems/complex-number-multiplication/

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        num2 = num2.split("+")
        num1[1] = num1[1].replace("i", "")
        num2[1] = num2[1].replace("i", "")
        for i in range(2):
            num1[i] = int(num1[i])
            num2[i] = int(num2[i])
        
        ans = ""
        ans += str(num1[0]*num2[0] - num1[1]*num2[1]) + "+"
        ans += str(num1[1]*num2[0] + num1[0]*num2[1]) + "i"
        
        return ans
        
