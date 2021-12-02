# https://leetcode.com/problems/four-divisors/

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        n = max(nums) + 1
        numDiv = [1]*n    
        sumDiv = [1]*n    
        
        for i in range(2, n):
            for j in range(i, n, i):
                numDiv[j] += 1
                sumDiv[j] += i
        
        ans = 0
        for num in nums: 
            if numDiv[num] == 4: 
                ans += sumDiv[num]
        
        return ans
        
