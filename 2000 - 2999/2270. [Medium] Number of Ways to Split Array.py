https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0
        
        left = 0
        right = sum(nums)
        
        for num in nums[: -1]:
            left += num
            right -= num
            
            if left >= right:
                ans += 1 
                
        return ans 
