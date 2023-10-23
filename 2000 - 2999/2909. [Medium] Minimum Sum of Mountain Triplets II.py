# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums) 
        
        left = [num for num in nums]
        right = [num for num in nums]
        
        for i in range(1, n):
            left[i] = min(left[i], left[i - 1])
            
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i], right[i + 1])
            
        ans = inf     
        
        for i in range(1, n - 1):
            if left[i - 1] < nums[i] and right[i + 1] < nums[i]:
                ans = min(ans, left[i - 1] + nums[i] + right[i + 1])
            
        return -1 if ans == inf else ans 
    
        
