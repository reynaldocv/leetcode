# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        ans = []
        for num in range(left, right + 1):
            DivideNumber = True
            for digit in str(num):
                if digit == "0" or num % int(digit) != 0:
                    DivideNumber = False
                    break
            if DivideNumber == True:
                ans.append(num)
        return ans
            
                    
