# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0: 
            return 0
        
        ans = 0         
        tmp = 0
        
        for _ in range(10):
            tmp += k             
            ans += 1 
            
            if tmp <= num and tmp % 10 == num % 10: 
                return ans 
            
        return -1
        
