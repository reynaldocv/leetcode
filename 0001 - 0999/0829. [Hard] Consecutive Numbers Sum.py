# https://leetcode.com/problems/consecutive-numbers-sum/

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        limit = int(sqrt(2*n))
        
        for num in range(1, limit + 1): 
            if (n - num*(num + 1)//2) % num == 0: 
                ans += 1
        
        return ans 
