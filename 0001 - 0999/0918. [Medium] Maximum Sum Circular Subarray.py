# https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        ans = cur = nums[0]
        for i in range(1, n):
            cur = nums[i] + max(cur, 0)
            ans = max(ans, cur)
        
        rightMaxSums = list(nums)
        
        rightSum = nums[-1]
        for i in range(n - 2, -1, -1):
            rightSum += nums[i]
            rightMaxSums[i] = max(rightMaxSums[i + 1], rightSum)
            
        leftSum = 0
        for i in range(n - 2):
            leftSum += nums[i]
            print(leftSum, rightMaxSums[i + 2])
            ans = max(ans, leftSum + rightMaxSums[i + 2])
            
        return ans
            
        
