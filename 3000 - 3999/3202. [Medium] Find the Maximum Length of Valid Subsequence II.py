# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0 for _ in range(k)] for _ in range(k)]
        
        ans = 0
        
        for num in nums: 
            x = num % k 
            
            for i in range(k):
                dp[x][i] = 1 + dp[i][x]

                ans = max(ans, dp[x][i])
        
        return ans
