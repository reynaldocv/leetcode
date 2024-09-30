# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

class Solution:
    def minElement(self, nums: List[int]) -> int:
        def helper(num):
            ans = 0 
            
            while num > 0:
                ans += (num % 10)
                
                num //= 10 
                
            return ans 
        
        return min(helper(num) for num in nums)
        
