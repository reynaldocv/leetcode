# https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [1, 1]
        ans = 1
        
        for i in range(1, n):
            B, A = 0, 0
            for j in range(i):
                if nums[j] < nums[i]:
                    A = max(A, dp[j][1])
                if nums[j] > nums[i]:
                    B = max(B, dp[j][0])
                    
            dp[i] = [A + 1, B + 1]
            ans = max(ans, max(A + 1, B + 1))
        
        return ans
        
        
