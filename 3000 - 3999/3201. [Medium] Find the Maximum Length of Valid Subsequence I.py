# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dp = [[0, 0], [0, 0]]
        
        ans = 0 
        
        for num in nums: 
            x = num % 2
            
            dp[x][0] = 1 + dp[0][x]; 
            dp[x][1] = 1 + dp[1][x]; 
            
            ans = max(ans, dp[x][0], dp[x][1])
        
        return ans 
            
