# https://leetcode.com/problems/largest-sum-of-averages/

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        def helper(i, j):
            return (left[j] - left[i])/(j - i)
            
        left = [0]
        for num in nums:
            left.append(left[-1] + num)
            
        n = len(nums)
        dp = [helper(i, n) for i in range(n)]
        
        for _ in range(k - 1):
            for i in range(n):
                for j in range(i + 1, n):
                    dp[i] = max(dp[i], helper(i, j) + dp[j])
                    
        return dp[0]
            
            
        
