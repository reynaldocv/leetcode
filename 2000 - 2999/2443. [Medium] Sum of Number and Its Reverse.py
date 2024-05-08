# https://leetcode.com/problems/sum-of-number-and-its-reverse/

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        n = len(str(num))
        
        start = 0 
        
        if n >= 2: 
            start = 10**(n - 2)
        
        for elem in range(start, num + 1): 
            tmp = elem + int(str(elem)[:: -1])
            
            if tmp == num: 
                return True 
            
        return False
            
            
        
