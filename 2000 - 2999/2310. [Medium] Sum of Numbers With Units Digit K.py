# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:        
        if num == 0: 
            return 0 
        
        total = 0
        for time in range(1, 11):
            total += k
            if total > num: 
                return -1 
            
            if (total % 10) == (num % 10):
                return time
            
        return -1
            
        
        
