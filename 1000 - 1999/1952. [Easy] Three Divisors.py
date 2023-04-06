# https://leetcode.com/problems/three-divisors/

class Solution:
    def isThree(self, n: int) -> bool:
        ans = 1
        
        for i in range(1, n):
            if n % i == 0:
                ans += 1 
                
        return ans == 3
                
                       

        
