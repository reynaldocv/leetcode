# https://leetcode.com/problems/longest-arithmetic-subsequence/

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        
        ans = 0
        
        for (i, numB) in enumerate(nums):
            for (j, numA) in enumerate(nums[:i]):
                ratio = numB - numA
                if ratio in dp[j]: 
                    dp[i][ratio] = dp[j][ratio] + 1
                else: 
                    dp[i][ratio] = 2
                    
                ans = max(ans, dp[i][ratio])
                
        return ans
        
