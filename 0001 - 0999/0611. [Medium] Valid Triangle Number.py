# https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums) 
        
        nums.sort() 
        
        ans = 0 
        
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                idx = bisect_left(nums, nums[i] + nums[j])
                
                ans += max(0, idx - j - 1)
                
        return ans 
    
