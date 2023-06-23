# https://leetcode.com/problems/find-triangular-sum-of-an-array/

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def helper(arr):
            n = len(arr)
            
            ans = []
            
            for i in range(n - 1):
                ans.append((arr[i] + arr[i + 1]) % 10)
                
            return ans 
        
        n = len(nums)
        
        for _ in range(n - 1):
            nums = helper(nums)
            
        return nums[0]
