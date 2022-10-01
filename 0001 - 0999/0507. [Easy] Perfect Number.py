# https://leetcode.com/problems/perfect-number/

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: 
            return False 
        
        limit = int(num**.5)
        divisors = set([1])
        
        for i in range(2, limit + 1):
            if num % i == 0: 
                divisors.add(i)
                divisors.add(num//i)
                    
        return sum(divisors) == num
            
            
        
        
