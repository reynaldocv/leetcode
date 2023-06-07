# https://leetcode.com/problems/maximum-or/

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        def helper(arr):
            ans = [0]
            
            for num in arr: 
                ans.append(ans[-1] | num)
                
            return ans 
        
        n = len(nums)
        
        left = helper(nums)
        right = helper(nums[:: -1])[:: -1]
        
        ans = 0 
        
        for i in range(n):
            l = left[i]
            r = right[i + 1]
            
            ans = max(ans, l | r | nums[i] << k)
            
        return ans 
