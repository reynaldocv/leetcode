https://leetcode.com/problems/rotate-function/

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        
        totalSum = 0 
        aSum = 0 
        
        for (i, num) in enumerate(nums):
            totalSum += (i + 1)*num 
            
            aSum += num 
            
        ans = -inf
        
        for num in nums: 
            tmp = totalSum - aSum            
            
            ans = max(ans, tmp)
            
            totalSum = tmp + num*n
            
        return ans 
            
            
        
        
