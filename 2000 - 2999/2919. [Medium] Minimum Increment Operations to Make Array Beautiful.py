# https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        dp = [0 for _ in range(n)]
        
        for i, num in enumerate(nums):
            dp[i] = max(0, k - num)
        
            if i - 3 >= 0:
                dp[i] += min(dp[i - 3], dp[i - 2], dp[i - 1]) 
        
        return min(dp[-1], dp[-2], dp[-3])
