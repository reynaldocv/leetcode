# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(start, end):
            arr = list(nums)
            ans = nums[start] if start < len(nums) else 0
            for i in range(start, end):
                max1 = arr[i - 2] if i - 2 >= start else 0
                max2 = arr[i - 3] if i - 3 >= start else 0
                arr[i] += max(max1, max2)
                ans = max(ans, arr[i])
                
            return ans
            
        n = len(nums)
        if n == 1:
            return nums[0]
        
        return max(helper(1, n), helper(2, n), helper(0, n - 1), helper(0, n - 2))
        
