# https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        dp = [1] + [0 for _ in range(target)]
        
        for num in nums: 
            for i in range(target, num - 1, -1):
                if dp[i - num] > 0: 
                    dp[i] = max(dp[i], dp[i - num] + 1)
            
        return dp[-1] -1
