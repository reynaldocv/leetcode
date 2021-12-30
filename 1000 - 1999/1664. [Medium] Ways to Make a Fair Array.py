# https://leetcode.com/problems/ways-to-make-a-fair-array/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        def helper(arr):            
            ans = [num for num in arr]
            for i in range(2, n):
                ans[i] += ans[i - 2]
                
            return ans
        
        n = len(nums)
        
        left = helper(nums)
        right = helper(nums[::-1])[::-1]
        
        ans = 0
        for i in range(n):
            l1 = 0 if i - 1 < 0 else left[i - 1]
            l2 = 0 if i - 2 < 0 else left[i - 2]
            r1 = 0 if i + 1 > n - 1 else right[i + 1]
            r2 = 0 if i + 2 > n - 1 else right[i + 2]
            
            if l1 + r2 == l2 + r1: 
                ans += 1
            
        return ans
