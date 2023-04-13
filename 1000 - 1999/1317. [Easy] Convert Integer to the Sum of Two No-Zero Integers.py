# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def helper(word):
            for char in str(word):
                if char == "0":
                    return False 
                
            return True 
        
        for a in range(1, n//2 + 1):
            b = n - a
            
            if helper(a) and helper(b):
                return [a, b]
        
          
        
            
