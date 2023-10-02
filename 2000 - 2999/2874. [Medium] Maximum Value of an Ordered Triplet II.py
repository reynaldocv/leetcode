# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums) 
        
        right = [nums[-1]]
        
        for i in range(n - 2, -1, -1):
            right.insert(0, max(right[0], nums[i]))
                 
        left = nums[0]
        
        ans = 0 
        
        for i in range(1, n - 1):
            ans = max(ans, (left - nums[i])*right[i + 1])
            
            left = max(left, nums[i])
            
        return ans 
