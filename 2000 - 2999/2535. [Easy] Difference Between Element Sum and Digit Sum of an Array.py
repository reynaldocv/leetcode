# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        @cache
        def helper(num):
            ans = 0 
            
            while num: 
                ans += (num % 10)
                
                num //= 10 
                
            return ans 
        
        aSum = 0 
        sumDigits = 0 
        
        for num in nums: 
            aSum += num 
            sumDigits += helper(num)
            
        return abs(aSum - sumDigits)
