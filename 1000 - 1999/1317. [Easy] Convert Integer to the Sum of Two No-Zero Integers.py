# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for numA in range(1, n):
            strA = str(numA)
            strB = str(n - numA)
            if "0" not in strA and "0" not in strB: 
                return [numA, n - numA]
            
          
        
            
