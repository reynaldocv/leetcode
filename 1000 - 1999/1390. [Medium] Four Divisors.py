# https://leetcode.com/problems/four-divisors/

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        limit = max(nums) + 1
        
        numDiv = [0 for _ in range(limit)]
        sumDiv = [0 for _ in range(limit)]
        
        for num in range(1, limit):
            for multiple in range(num, limit, num):
                numDiv[multiple] += 1 
                sumDiv[multiple] += num 
                
        ans = 0     
            
        for num in nums: 
            if numDiv[num] == 4: 
                ans += sumDiv[num]
                
        return ans 
                
        
