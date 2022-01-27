# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)        
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]
        
        for i in range(1, n):
            val = 0 
            for j in range(i):
                if nums[j] < nums[i]:
                    val = max(val, left[j] + 1)
        
            left[i] = val
            
        for i in range(n - 2, -1, -1):
            val = 0 
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    val = max(val, right[j] + 1)
            
            right[i] = val
            
        ans = inf
        
        for i in range(1, n - 1):
            if left[i] > 0 and right[i] > 0:
                ans = min(ans, n - 1 - left[i] - right[i])    
        
        return ans
