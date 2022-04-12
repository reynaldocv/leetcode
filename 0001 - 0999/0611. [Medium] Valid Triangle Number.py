# https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums.sort()        
        ans = 0 
        
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                minElem = nums[j] - nums[i]
                maxElem = nums[j] + nums[i]
                
                end = bisect_left(nums, maxElem)                
                if end <= j: 
                    break 
                
                start = max(j + 1, bisect_left(nums, minElem + 1))
                
                ans += end - start 
        
        return ans 
    
